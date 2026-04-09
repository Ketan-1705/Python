from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Category, Tag, Comment, Like, Follow, Profile
from .forms import PostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, "Account created successfully! Please login.")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def home(request):
    posts = Post.objects.all().order_by('-created_at')

    author = request.GET.get('author')
    category = request.GET.get('category')
    start = request.GET.get('start')
    end = request.GET.get('end')

    if author:
        posts = posts.filter(author__username=author)
    if category:
        posts = posts.filter(category__name=category)
    if start and end:
        posts = posts.filter(created_at__range=[start, end])

    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def create_post(request):
    # Check if user has author role
    try:
        if request.user.profile.role != 'author' and not request.user.is_superuser:
            messages.error(request, "Only Authors can create posts.")
            return redirect('home')
    except Profile.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "Post created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        messages.info(request, "Unliked post.")
    else:
        messages.success(request, "Liked post!")
    return redirect('home')

@login_required
def follow_user(request, user_id):
    target = get_object_or_404(User, id=user_id)
    if target == request.user:
        messages.warning(request, "You cannot follow yourself.")
        return redirect('home')
        
    follow, created = Follow.objects.get_or_create(follower=request.user, following=target)
    if not created:
        follow.delete()
        messages.info(request, f"Unfollowed {target.username}.")
    else:
        messages.success(request, f"Now following {target.username}!")
    return redirect('home')

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment added!")
    return redirect('home') # Adjust according to detail view if exists

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id, user=request.user)
    comment.delete()
    messages.info(request, "Comment deleted.")
    return redirect('home')

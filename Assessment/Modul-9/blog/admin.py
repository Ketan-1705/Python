from django.contrib import admin
from .models import Category, Tag, Post, Comment, Like, Follow, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
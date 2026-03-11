from django.shortcuts import render
from .models import Contact,User
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method=="POST":
        Contact.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        remark=request.POST['remark']
        )
        msg="contect details submitted successfully"
        contact=Contact.objects.all().order_by("-id")[:3]
        return render(request,'contact.html',{'msg':msg,'contact':contact})
    else:
        contact=Contact.objects.all().order_by("-id")[:3]
        return render(request,'contact.html',{'contact':contact})
def signup(request):
    try:
        User.objects.get(email=request.POST['email'])
        msg="email already exist"   
        return render(request,'signup.html',{'msg':msg})
    except:
        if request.POST['password']==request.POST['c_password']:
            User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mo xbile'],
            address=request.POST['address'],
            password=request.POST['password']
            )
            msg="signup details submitted successfully"
            return render(request,'signup.html',{'msg':msg})
        else:
            msg="password and confirm password does not match"
            return render(request,'signup.html',{'msg':msg})
def login(request):
   return render(request,'login.html')  
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'index.html')

def user_home(request):
    return render(request,'home.html')

def loginn(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
    return render(request,'login.html')

def createuser(request):
    if request.method == 'POST':
        username=request.POST['uid']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'createuser.html')
        
    

from tabnanny import check
from unittest.case import DIFF_OMITTED
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
# Create your views here {ID-manas@1 and PASSWORD-1234567890!@}

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
       # check if userhas entered correct credentials
       username= request.POST.get('username')
       password= request.POST.get('password')


       user = authenticate(request,username=username, password=password)


       if user is not None:
        login(request, user)
        return redirect("/")
       else:
        return render(request,'login.html')

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login") 
    
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import auth

#Create your views here.

def signup_view(request):

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('email')
        email = request.POST.get('username')
        password = request.POST["password"]
        re_password = request.POST.get('re_password')
        birth = request.POST.get('birth')

        user = User.objects.create_user(username, email, password)
        user.birth = birth
        user.re_password = re_password
        user.save()

        return redirect("/")

    return render(request, "users/signup.html")

def login_view(request):
     if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST["password"]
         user = authenticate(username=username, password=password)
         if user is not None:
             print("인증 성공")
             login(request, user)
         else:
             print("인증 실패")

     return render(request, "users/login.html")

def introduce_view(request):
    
    return render(request, "users/introduce.html")

def policy_view(request):
    
    return render(request, "users/policy.html")

def logout(request):
    if request.method == "POST" :
        auth.logout(request)
        return render(request, "users/login.html")

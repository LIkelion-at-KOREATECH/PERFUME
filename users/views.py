from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User


#Create your views here.

def signup_view(request):

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        birth = request.POST.get('birth')

        user.username = username
        user.email = email
        user.password = password
        user.birth = birth
        user.save()

        return render(request, "users/login.html")

    return render(request, "users/signup.html")

def login_view(request):
     if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST.get('password')
         print(username)
         print(password)
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
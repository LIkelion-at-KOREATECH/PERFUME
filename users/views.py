from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import User
from django.contrib import auth
from django.contrib.auth import login


#Create your views here.

def signup(request):
    res_data={}
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        re_password = request.POST.get('re_password', False)
        birth = request.POST.get('birth', False)
        if password != re_password :
            return render(request, 'signup.html' , {'error' : 'password incorrect!'})
        else:
           user = User.objects.create_user(username, email, password)
           user.birth = birth
           user.save()

           return redirect('/')

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            print("인증 성공")
            auth.login(request, user)
            response = render,(request, 'home.html')
            response.set_cookie('email', email)
            resaponse.set_cookie('password', password)
            return  response

        else:
            print("인증 실패")
            return  render (request, 'login.html', {'error': 'email or password is incorrect'})
    else :

       return render(request, 'login.html')

def home(request):

    return render(request, "home.html")

def introduce(request):
    
    return render(request, 'introduce.html')

def policy(request):
    
    return render(request, 'policy.html')

def logout(request):
    if request.method == "POST" :
        auth.logout(request)
        return redirect('/')

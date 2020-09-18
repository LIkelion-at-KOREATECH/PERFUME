from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import User , Blog
from django.contrib import auth
from django.contrib.auth import login


#Create your views here.

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        re_password = request.POST.get('re_password', False)
        birth = request.POST.get('birth', False)
        if password != re_password :
            return render(request, 'signup.html' , {'error' : 'password incorrect!'})
        else:
           user = User.objects.create_user(email, password)
           user.birth = birth
           user.re_password = re_password
           user.name = name
           user.save()

           return redirect('/')

    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print("인증 성공")
            auth.login(request, user)
            response = render(request, 'choose.html')
            response.set_cookie('email', email)
            response.set_cookie('password', password)
            return response
        else:
            print("인증 실패")
            return  render (request, 'login.html')
    return render(request, "login.html")

def introduce(request):
    
    return render(request, 'introduce.html')

def policy(request):
    
    return render(request, 'policy.html')

def logout(request):
    if request.method == "POST" :
        auth.logout(request)
        return redirect('/', {'caution':'로그아웃 되었습니다'})
        
# 게시글 페이지 연동

def choose(request):
    return render(request,'choose.html')

def choose_atm(request):
    return render(request, 'choose_atm.html')

def choose3(request):
    return render(request,'choose3.html')

def home(request):
    blogs=Blog.objects #전달받은 객체 (쿼리셋) 
    return render(request, 'home.html', {'blogs':blogs})

def post(request):
    if request.method == "GET":
        return render(request, 'post.html')
    elif request.method == "POST":
        image = request.FILES.get('image', None)
        address = request.POST.get('address', None)
        atm = request.POST.get('atm', None)
        name = request.POST.get('name', None)
        title = request.POST.get('title', None)
        body = request.POST.get('body', None)
        
        blog = Blog(image=image, address=address, atm=atm, name=name, title=title, body=body)
        blog.save()

        return render(request, 'home.html')

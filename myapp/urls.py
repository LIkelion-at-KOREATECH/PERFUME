"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from users.views import login_view
from users.views import signup_view
from users.views import introduce_view
from users.views import policy_view
from users import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('introduce/', introduce_view, name="introduce"),
    path('policy/', policy_view, name="policy"),
    path('logout/', views.logout, name="logout"),
]
from django.urls import path
from . import views
#from django.conf.urls import include


urlpatterns = [
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('introduce/', views.introduce, name="introduce"),
    path('policy/', views.policy, name="policy"),
    path('logout/', views.logout, name="logout"),
    path('choose/', views.choose, name="choose"),
    path('atm/', views.choose_atm, name="choose_atm"),
    path('choose3/', views.choose3, name="choose3"),
    path('home/',views.home, name="home"),
]
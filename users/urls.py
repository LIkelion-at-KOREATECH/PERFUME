from django.urls import path
from . import views
#from django.conf.urls import include


urlpatterns = [
    path("login", views.login_view)
]
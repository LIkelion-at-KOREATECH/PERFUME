from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class User(AbstractUser):

   username = None
   
   name = models.CharField(default="name", max_length=64)
   email = models.CharField(default="email", max_length=64)
   password = models.CharField(default="password", max_length=64)
   birth = models.CharField(default="birth", max_length=8)

   objects = UserManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []


   def __str__(self): 
        return self.name


class Blog(models.Model):
    address = models.CharField(max_length = 100)
    name=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    image = models.ImageField('img/')
    pub_date=models.DateTimeField('date published')
    body = models.TextField()


    def __str__(self):
        return self.title
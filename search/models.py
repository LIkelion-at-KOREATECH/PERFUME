from django.db import models

# Create your models here.

# class Post(models.Model):
class Blog(models.Model):
    image = models.ImageField(blank=True, upload_to='media/')
    address = models.CharField(max_length = 100)
    atm = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    body = models.TextField()
    registered_dttm = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
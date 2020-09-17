from django.db import models

# Create your models here.

# class Post(models.Model):
class Blog(models.Model):
    image = models.ImageField(upload_to = 'img/')
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

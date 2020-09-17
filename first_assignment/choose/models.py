from django.db import models

# Create your models here.

class Blog(models.Model):
    address = models.CharField(max_length = 100)
    name=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    image = models.ImageField('img/')
    pub_date=models.DateTimeField('date published')
    body = models.TextField()


    def __str__(self):
        return self.title
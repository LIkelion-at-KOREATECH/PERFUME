from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to = 'images/')
    username = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.username
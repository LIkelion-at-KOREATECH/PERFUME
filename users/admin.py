from django.contrib import admin
from .models import User
from .models import Blog
from . import models

# Register your models here.

admin.site.register(User)

admin.site.register(Blog)
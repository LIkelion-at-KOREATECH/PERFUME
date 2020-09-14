from django.contrib import admin
from django.urls import path
import choose.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', choose.views.choose, name="choose"),
]

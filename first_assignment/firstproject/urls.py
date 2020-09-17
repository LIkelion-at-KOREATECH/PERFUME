from django.contrib import admin
from django.urls import path
import choose.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', choose.views.choose, name="choose"),
    path('atm/',choose.views.choose_atm, name="choose_atm"),
    path('choose/',choose.views.choose3, name="choose3"),
    path('home/',choose.views.home, name="home"),
]

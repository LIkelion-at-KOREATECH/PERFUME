from django.contrib import admin
from django.urls import path
import choose.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', choose.views.choose, name="choose"),
    path('atm/',choose.views.choose_atm, name="choose_atm"),
    path('choose/',choose.views.choose3, name="choose3"),
    path('home/',choose.views.home, name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


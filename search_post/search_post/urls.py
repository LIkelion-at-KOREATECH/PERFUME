from django.contrib import admin
from django.urls import path
import search.views

# media 불러오기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search.views.search, name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from web.views import HomeView, BlogView, ThoughtsView
from web.views import markdown_uploader

urlpatterns = [
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('api/uploader/', markdown_uploader, name='markdown_uploader_page'),
    path('tinymce/', include('tinymce.urls')),
    path('filer/', include('filer.urls')),
    path('', HomeView.as_view(), name='home'),
    path('blog', BlogView.as_view(), name='blog'),
    path('thoughts', ThoughtsView.as_view(), name='thoughts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
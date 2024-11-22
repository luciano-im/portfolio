from django.contrib import admin
from django.urls import path, include

from web.views import HomeView
from web.views import markdown_uploader

urlpatterns = [
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('api/uploader/', markdown_uploader, name='markdown_uploader_page'),
    path('', HomeView.as_view(), name='home'),
]


from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
# from django.contrib.sitemaps import GenericSitemap
from main.sitemaps import BlogSitemap
from .models import Blog


sitemaps = {
    'blogs': BlogSitemap
}

app_name = 'main'

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='home'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('blog', views.BlogView.as_view(), name='blogs'),
    path('sitemap.xml', sitemap, {"sitemaps" :sitemaps }, name= "django.contrib.sitemaps.views.sitemap") ,
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog'),
]
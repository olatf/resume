

from django.contrib.sitemaps import Sitemap
from .models import Blog


class BlogSitemap(Sitemap):
    def blogs(self):
        return Blog.objects.all()
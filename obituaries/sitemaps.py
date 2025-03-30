from django.contrib.sitemaps import Sitemap
from .models import Obituary

class ObituarySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    
    def items(self):
        return Obituary.objects.all()
    
    def lastmod(self, obj):
        return obj.submission_date
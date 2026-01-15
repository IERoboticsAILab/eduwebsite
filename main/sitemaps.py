from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project, ResearchLine


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['about', 'experience', 'projects', 'publications', 'courses', 'talks', 'contact']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse('project_detail', args=[obj.slug])

    def lastmod(self, obj):
        return obj.updated_at


class ResearchLineSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return ResearchLine.objects.all()

    def location(self, obj):
        return reverse('research_detail', args=[obj.slug])

    def lastmod(self, obj):
        return obj.updated_at

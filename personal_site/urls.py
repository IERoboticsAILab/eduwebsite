"""
URL configuration for personal_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.views.generic import TemplateView

from main import views
from main.sitemaps import StaticViewSitemap, ProjectSitemap, ResearchLineSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
    'research': ResearchLineSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.about, name="about"),
    path("experience/", views.experience, name="experience"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("research-lines/<slug:slug>/", views.research_detail, name="research_detail"),
    path("publications/", views.publications, name="publications"),
    path("courses/", views.courses, name="courses"),
    path("talks/", views.talks, name="talks"),
    path("contact/", views.contact, name="contact"),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name="sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

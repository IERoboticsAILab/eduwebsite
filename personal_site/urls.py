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
from django.urls import path

from main import views

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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

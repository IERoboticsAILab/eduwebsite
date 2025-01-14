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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Language switch URL
]

# Wrap your existing URLs with i18n_patterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('work/', views.work, name='work'),
    path('publications/', views.publications, name='publications'),
    path('talks/', views.talks, name='talks'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('contact/', views.contact, name='contact'),
    prefix_default_language=True,  # Changed to True to ensure consistent URL patterns
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

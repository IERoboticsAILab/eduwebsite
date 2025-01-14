from django.shortcuts import render
from .models import Project, Publication
from django.core.paginator import Paginator

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def education(request):
    return render(request, 'main/education.html')

def work(request):
    return render(request, 'main/work.html')

def talks(request):
    return render(request, 'main/talks.html')

def blog(request):
    return render(request, 'main/blog.html')

def contact(request):
    return render(request, 'main/contact.html')

def projects(request):
    projects_list = Project.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(projects_list, 6)  # Show 6 projects per page
    projects = paginator.get_page(page_number)

    if request.htmx:
        return render(request, 'main/partials/project-list.html', {'projects': projects})
    return render(request, 'main/projects.html', {'projects': projects})

def publications(request):
    publications_list = Publication.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(publications_list, 6)  # Show 6 projects per page
    publications = paginator.get_page(page_number)

    if request.htmx:
        return render(request, 'main/partials/publication-list.html', {'publications': publications})
    return render(request, 'main/publications.html', {'publications': publications})

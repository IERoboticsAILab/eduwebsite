from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    projects_list = Project.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(projects_list, 6)  # Show 6 projects per page
    projects = paginator.get_page(page_number)

    if request.htmx:
        return render(request, 'main/partials/project-list.html', {'projects': projects})
    return render(request, 'main/projects.html', {'projects': projects})

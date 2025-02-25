from django.core.paginator import Paginator
from django.db.models import Q, DateTimeField
from django.db.models.functions import ExtractYear
from django.shortcuts import get_object_or_404, render

from .models import (EducationItem, ExperienceDescription, IntroText,
                     OpenPositions, Project, Publication, Talk, WorkItem)


def about(request):
    intro_text = IntroText.objects.first()
    return render(request, "main/about.html", {"intro_text": intro_text})


def talks(request):
    talks = Talk.objects.all()
    return render(request, "main/talks.html", {"talks": talks})


def contact(request):
    open_positions = OpenPositions.objects.all()
    return render(request, "main/contact.html", {"open_positions": open_positions})


def projects(request):
    projects_list = Project.objects.all()
    page_number = request.GET.get("page", 1)
    paginator = Paginator(projects_list, 6)
    projects = paginator.get_page(page_number)

    if request.htmx:
        return render(
            request, "main/partials/project-list.html", {"projects": projects}
        )
    return render(request, "main/projects.html", {"projects": projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "main/project_detail.html", {"project": project})


def publications(request):
    search_query = request.GET.get('search', '')
    selected_year = request.GET.get('year')
    
    # Get all distinct years as integers
    years = Publication.objects.annotate(
        year=ExtractYear('publication_date')
    ).order_by('-year').values_list('year', flat=True).distinct()
    
    publications_list = Publication.objects.all()
    
    # Apply year filter
    if selected_year and selected_year != 'all':
        publications_list = publications_list.filter(publication_date__year=int(selected_year))
    
    # Apply search filter
    if search_query:
        publications_list = publications_list.filter(
            Q(title__icontains=search_query) |
            Q(authors__icontains=search_query) |
            Q(journal__icontains=search_query) |
            Q(abstract__icontains=search_query) |
            Q(keywords__name__icontains=search_query)
        ).distinct()

    paginator = Paginator(publications_list, 6)
    page_number = request.GET.get("page", 1)
    publications = paginator.get_page(page_number)

    context = {
        "publications": publications,
        "search_query": search_query,
        "years": years,
        "selected_year": selected_year,
    }

    if request.htmx:
        return render(request, "main/partials/publication-list.html", context)
    return render(request, "main/publications.html", context)

def experience(request):
    education_items = EducationItem.objects.all()
    work_items = WorkItem.objects.all()
    experience_description = ExperienceDescription.objects.first()
    return render(
        request,
        "main/experience.html",
        {
            "education_items": education_items,
            "work_items": work_items,
            "experience_description": experience_description,
        },
    )

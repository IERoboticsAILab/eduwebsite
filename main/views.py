from django.shortcuts import render, get_object_or_404
from .models import (
    Project,
    Publication,
    IntroText,
    EducationItem,
    WorkItem,
    Talk,
    ExperienceDescription,
    OpenPositions,
)
from django.core.paginator import Paginator


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
    publications_list = Publication.objects.all()
    page_number = request.GET.get("page", 1)
    paginator = Paginator(publications_list, 6)
    publications = paginator.get_page(page_number)

    if request.htmx:
        return render(
            request,
            "main/partials/publication-list.html",
            {"publications": publications},
        )
    return render(request, "main/publications.html", {"publications": publications})


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

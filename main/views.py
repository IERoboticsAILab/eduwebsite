from django.shortcuts import render, get_object_or_404
from .models import Project, Publication, BlogPost
from django.core.paginator import Paginator
import markdown

def about(request):
    return render(request, 'main/about.html')

def education(request):
    return render(request, 'main/education.html')

def work(request):
    return render(request, 'main/work.html')

def talks(request):
    return render(request, 'main/talks.html')

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'main/blog.html', {'blog_posts': blog_posts})

def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.content = markdown.markdown(post.content)  # Convert Markdown to HTML
    return render(request, 'main/blog_post_detail.html', {'post': post})

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

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})

def publications(request):
    publications_list = Publication.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(publications_list, 6)  # Show 6 projects per page
    publications = paginator.get_page(page_number)

    if request.htmx:
        return render(request, 'main/partials/publication-list.html', {'publications': publications})
    return render(request, 'main/publications.html', {'publications': publications})

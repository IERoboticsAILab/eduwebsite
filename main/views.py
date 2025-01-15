from django.shortcuts import render, get_object_or_404
from .models import Project, Publication
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

def about(request):
    return render(request, 'main/about.html')

def education(request):
    return render(request, 'main/education.html')

def work(request):
    return render(request, 'main/work.html')

def talks(request):
    return render(request, 'main/talks.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Compose email message
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=f"Contact Form: {subject}",
                message=email_message,
                from_email=email,
                recipient_list=['your-email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again.')

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

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

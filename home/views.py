from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    all_projects = Project.objects.all()
    return render(request, 'home/index.html', {'all_projects' : all_projects})

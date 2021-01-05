from django.shortcuts import render
from .models import Project, Technology


# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    technologies = Technology.objects.filter(categories__in = projects).distinct()
    context = {
        'projects': projects,
        'technologies': technologies,
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def projects_sorted(request, technology):
    project = Project.objects.filter(technology__name__contains=technology)
    context = {
        'projects': project,
        'technology': technology,
    }
    return render(request, 'projects_sorted.html', context)

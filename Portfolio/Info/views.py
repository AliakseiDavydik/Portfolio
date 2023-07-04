from django.shortcuts import render
from django.views.generic.base import View
from .models import AboutProject, About_me


# Create your views here.:
def project_index(request):
    projects = AboutProject.objects.all()
    return render(request, "project_index.html", {"info_projects": projects})


def project_detail(request, pk):
    project = AboutProject.objects.get(pk=pk)
    return render(request, "project_detail.html", {"info_project": project})


def index_me(request):
    about = About_me.objects.all()
    return render(request, "index.html", {"user_info": about})


from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Heading, PersonalDetail


def display_home(request):
    headings = Heading.objects.all()
    context = {'headings': headings}
    return render(request, 'pages/index.html', context)


def display_about(request):
    details = PersonalDetail.objects.all()
    context = {'details': details}
    return render(request, 'pages/about.html', context)

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Home, PersonalDetail


def display_home(request):
    data = Home.objects.all()
    context = {'data': data}
    return render(request, 'pages/index.html', context)


def display_about(request):
    details = PersonalDetail.objects.all()
    context = {'details': details}
    return render(request, 'pages/about.html', context)

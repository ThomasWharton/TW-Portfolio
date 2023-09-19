from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Heading


def display_home(request):
    headings = Heading.objects.all()
    context = {'headings': headings}
    return render(request, 'pages/index.html', context)


# def display_home(request):
#     data = Heading.objects.all()
#     context = {'data': data}
#     return render(request, 'pages/index.html', context)

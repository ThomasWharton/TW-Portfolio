from django.shortcuts import render, get_object_or_404, redirect
from .models import Home, PersonalDetail
from django.http import HttpResponseRedirect


def check_admin(fn):
    def wrapper(request):
        if request.user.is_superuser:
            return fn(request)
        else:
            return HttpResponseRedirect('/')

    return wrapper


def display_home(request):
    data = Home.objects.all()
    context = {'data': data}
    return render(request, 'pages/index.html', context)


def display_about(request):
    details = PersonalDetail.objects.all()
    context = {'details': details}
    return render(request, 'pages/about.html', context)


@check_admin
def display_dashboard(request):
    return render(request, 'pages/dashboard.html')

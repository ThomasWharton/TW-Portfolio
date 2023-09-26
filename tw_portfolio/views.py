from django.shortcuts import render, get_object_or_404, redirect
from .models import Home, PersonalDetail
from django.http import HttpResponseRedirect
from .forms import PersonalDetailForm


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


@check_admin
def display_edit_personal_detail(request):
    detail = get_object_or_404(PersonalDetail)
    data = PersonalDetail.objects.all()

    if request.method == 'POST':
        personal_detail_form = PersonalDetailForm(request.POST, request.FILES, instance=detail)
        if personal_detail_form.is_valid():
            personal_detail_form.save()
            return redirect('edit-personal-detail')
    else:
        personal_detail_form = PersonalDetailForm(instance=detail)

    context = {
        'data': data,
        'personal_detail_form': personal_detail_form
    }

    return render(request, 'pages/edit_personal_detail.html', context)

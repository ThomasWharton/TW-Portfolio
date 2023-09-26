from django.shortcuts import render, get_object_or_404, redirect
from .models import Home, PersonalDetail, Skill, SkillCategory, Project, WorkHistory, Education
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


def display_all(request):
    detail = PersonalDetail.objects.all()
    skill = Skill.objects.all()
    category = SkillCategory.objects.all()
    project = Project.objects.all()
    data = Home.objects.all()
    context = {
        'detail': detail, 'data': data, 'project': project, 'skill': skill, 'category': category
        }
    if request.path == "home/":
        return render(request, 'pages/index.html', context )
    else: 
        return render(request, 'pages/index.html', context )

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

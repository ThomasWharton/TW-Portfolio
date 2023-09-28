from django.shortcuts import render, get_object_or_404, redirect
from .models import Home, PersonalDetail, Skill, SkillCategory, Project, WorkHistory, Education
from django.http import HttpResponseRedirect
from .forms import PersonalDetailForm, SkillForm, HomeForm, ProjectForm, WorkHistoryForm, EducationForm


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


def display_all(request):
    detail = PersonalDetail.objects.all()
    skill = Skill.objects.all()
    category = SkillCategory.objects.all()
    project = Project.objects.all()
    data = Home.objects.all()
    work_history = WorkHistory.objects.all()
    education = Education.objects.all()

    context = {
        'detail': detail,
        'data': data,
        'project': project,
        'skill': skill,
        'category': category,
        'work_history': work_history,
        'education': education
        }
    if request.path == "home/":
        return render(request, 'pages/index.html', context)
    else:
        return render(request, 'pages/index.html', context)


@check_admin
def display_dashboard(request):
    return render(request, 'pages/dashboard.html')


@check_admin
def display_edit_home(request):
    data = get_object_or_404(Home)
    detail = Home.objects.all()

    if request.method == 'POST':
        home_form = HomeForm(request.POST, request.FILES, instance=data)
        if home_form.is_valid():
            home_form.save()
            return redirect('dashboard')
    else:
        home_form = HomeForm(instance=data)

    context = {
        'detail': detail,
        'home_form': home_form
    }

    return render(request, 'pages/edit_home.html', context)


@check_admin
def display_edit_personal_detail(request):
    data = get_object_or_404(PersonalDetail)
    detail = PersonalDetail.objects.all()

    if request.method == 'POST':
        personal_detail_form = PersonalDetailForm(request.POST, request.FILES, instance=data)
        if personal_detail_form.is_valid():
            personal_detail_form.save()
            return redirect('dashboard')
    else:
        personal_detail_form = PersonalDetailForm(instance=data)

    context = {
        'detail': detail,
        'personal_detail_form': personal_detail_form
    }

    return render(request, 'pages/edit_personal_detail.html', context)


@check_admin
def display_add_skill(request):
    if request.method == 'POST':
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill_form.save()
            return redirect('dashboard')

    context = {
        'skill_form': SkillForm(),
    }

    return render(request, 'pages/add_skill.html', context)


@check_admin
def display_add_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.project_image = request.FILES['project_image']
            project_form.save()
            return redirect('dashboard')
        else:
            project_form = ProjectForm()

    project = Project.objects.all()

    context = {
        'project': project,
        'project_form': ProjectForm(),
    }

    return render(request, 'pages/add_project.html', context)


@check_admin
def display_add_work_history(request):
    if request.method == 'POST':
        work_history_form = WorkHistoryForm(request.POST)
        if work_history_form.is_valid():
            work_history_form.save()
            return redirect('dashboard')

    context = {
        'work_history_form': WorkHistoryForm(),
    }

    return render(request, 'pages/add_work_history.html', context)


@check_admin
def display_add_education(request):
    if request.method == 'POST':
        education_form = EducationForm(request.POST)
        if education_form.is_valid():
            education_form.save()
            return redirect('dashboard')

    context = {
        'education_form': EducationForm(),
    }

    return render(request, 'pages/add_education.html', context)
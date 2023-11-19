from django.shortcuts import render, get_object_or_404, redirect
from .models import Home, PersonalDetail, Skill, SkillCategory, Project, WorkHistory, Education
from django.http import HttpResponseRedirect
from .forms import PersonalDetailForm, SkillForm, HomeForm, ProjectForm, WorkHistoryForm, EducationForm
from django.contrib import messages


def check_admin(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return fn(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

    return wrapper


def display_home(request):
    data = Home.objects.all()
    context = {'data': data}
    return render(request, 'pages/index.html', context)


def display_all(request):
    details = PersonalDetail.objects.all()
    skills = Skill.objects.all()
    categories = SkillCategory.objects.all()
    projects = Project.objects.all()
    data = Home.objects.all()
    work_histories = WorkHistory.objects.all()
    educations = Education.objects.all()

    context = {
        'details': details,
        'data': data,
        'projects': projects,
        'skills': skills,
        'categories': categories,
        'work_histories': work_histories,
        'educations': educations
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
            messages.success(request, "Home details edited successfully!")
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
            messages.success(request, "Personal details edited successfully!")
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
            messages.success(request, "Skill added successfully!")
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
            messages.success(request, "Project added successfully!")
            return redirect('dashboard')
        else:
            project_form = ProjectForm()

    projects = Project.objects.all()

    context = {
        'projects': projects,
        'project_form': ProjectForm(),
    }

    return render(request, 'pages/add_project.html', context)


@check_admin
def display_add_work_history(request):
    if request.method == 'POST':
        work_history_form = WorkHistoryForm(request.POST)
        if work_history_form.is_valid():
            work_history_form.save()
            messages.success(request, "Work history added successfully!")
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
            messages.success(request, "Education information added successfully!")
            return redirect('dashboard')

    context = {
        'education_form': EducationForm(),
    }

    return render(request, 'pages/add_education.html', context)


@check_admin
def display_edit_skill(request, skill_id=None):
    skills = Skill.objects.all()
    categories = SkillCategory.objects.all()

    if skill_id:
        skill = get_object_or_404(Skill, pk=skill_id)
        skill_form = SkillForm(instance=skill)
    else:
        skill_form = SkillForm()

    if request.method == 'POST':
        if skill_id:
            skill = get_object_or_404(Skill, pk=skill_id)
            skill_form = SkillForm(request.POST, request.FILES, instance=skill)
        else:
            skill_form = SkillForm(request.POST, request.FILES)

        if skill_form.is_valid():
            skill_form.save()
            messages.success(request, "Skill edited successfully!")
            return redirect('dashboard')

    context = {
        'skill': skill if skill_id else None,
        'skill_form': skill_form,
        'categories': categories,
        'skills': skills
    }

    return render(request, 'pages/edit_skill.html', context)


@check_admin
def display_edit_project(request, project_id=None):
    projects = Project.objects.all()

    if project_id:
        project = get_object_or_404(Project, pk=project_id)
        project_form = ProjectForm(instance=project)
    else:
        project_form = ProjectForm()

    if request.method == 'POST':
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            project_form = ProjectForm(request.POST, request.FILES, instance=project)
        else:
            project_form = ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            project_form.save()
            messages.success(request, "Project edited successfully!")
            return redirect('dashboard')

    context = {
        'project': project if project_id else None,
        'project_form': project_form,
        'projects': projects
    }

    return render(request, 'pages/edit_project.html', context)


@check_admin
def display_edit_work_history(request, work_history_id=None):
    work_histories = WorkHistory.objects.all()

    if work_history_id:
        work_history = get_object_or_404(WorkHistory, pk=work_history_id)
        work_history_form = WorkHistoryForm(instance=work_history)
    else:
        work_history_form = WorkHistoryForm()

    if request.method == 'POST':
        if work_history_id:
            work_history = get_object_or_404(WorkHistory, pk=work_history_id)
            work_history_form = WorkHistoryForm(request.POST, instance=work_history)
        else:
            work_history_form = WorkHistoryForm(request.POST)

        if work_history_form.is_valid():
            work_history_form.save()
            messages.success(request, "Work history edited successfully!")
            return redirect('dashboard')

    context = {
        'work_history': work_history if work_history_id else None,
        'work_history_form': work_history_form,
        'work_histories': work_histories
    }

    return render(request, 'pages/edit_work_history.html', context)


@check_admin
def display_edit_education(request, education_id=None):
    educations = Education.objects.all()

    if education_id:
        education = get_object_or_404(Education, pk=education_id)
        education_form = EducationForm(instance=education)
    else:
        education_form = EducationForm()

    if request.method == 'POST':
        if education_id:
            education = get_object_or_404(Education, pk=education_id)
            education_form = EducationForm(request.POST, instance=education)
        else:
            education_form = EducationForm(request.POST)

        if education_form.is_valid():
            education_form.save()
            messages.success(request, "Education edited successfully!")
            return redirect('dashboard')

    context = {
        'education': education if education_id else None,
        'education_form': education_form,
        'educations': educations
    }

    return render(request, 'pages/edit_education.html', context)


@check_admin
def display_delete_skill(request, skill_id=None):
    skills = Skill.objects.all()
    categories = SkillCategory.objects.all()

    if skill_id:
        skill = get_object_or_404(Skill, pk=skill_id)
        skill_form = SkillForm(instance=skill)
    else:
        skill_form = SkillForm()

    if request.method == 'POST':
        if skill_id:
            skill.delete()
            messages.success(request, "Skill deleted successfully!")
            return redirect('dashboard')

    context = {
        'skill': skill if skill_id else None,
        'skill_form': skill_form,
        'categories': categories,
        'skills': skills
    }

    return render(request, 'pages/delete_skill.html', context)


@check_admin
def display_delete_project(request, project_id=None):
    projects = Project.objects.all()

    if project_id:
        project = get_object_or_404(Project, pk=project_id)
        project_form = ProjectForm(instance=project)
    else:
        project_form = ProjectForm()

    if request.method == 'POST':
        if project_id:
            project.delete()
            messages.success(request, "Project deleted successfully!")
            return redirect('dashboard')

    context = {
        'project': project if project_id else None,
        'project_form': project_form,
        'projects': projects
    }

    return render(request, 'pages/delete_project.html', context)
from django import forms
from .models import PersonalDetail, Home, Project, Skill, WorkHistory, Education


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'


class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = '__all__'


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class WorkHistoryForm(forms.ModelForm):
    class Meta:
        model = WorkHistory
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

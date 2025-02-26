from django import forms
from .models import PersonalDetail, Home, Project, Skill, WorkHistory, Education


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['brief_description']
        widgets = {
            'brief_description': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
        }


class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = [
            'detail_paragraph_1',
            'detail_paragraph_2',
            'full_name',
            'nationality',
            'residence'
        ]
        widgets = {
            'detail_paragraph_1': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
            'detail_paragraph_2': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
            'full_name': forms.TextInput(attrs={'style': 'max-width:20rem'}),
            'nationality': forms.TextInput(attrs={'style': 'max-width:20rem'}),
            'residence': forms.TextInput(attrs={'style': 'max-width:20rem'})
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'style': 'max-width:20rem'}),
            'skill_description': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
            'skill_competency': forms.TextInput(attrs={'style': 'max-width:20rem'}),
        }


class SelectSkillForm(forms.ModelForm):
    class Meta:
        model: Skill
        fields = ['name']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'style': 'max-width:20rem'}),
            'project_description': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
        }


class WorkHistoryForm(forms.ModelForm):
    class Meta:
        model = WorkHistory
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

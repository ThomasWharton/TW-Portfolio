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

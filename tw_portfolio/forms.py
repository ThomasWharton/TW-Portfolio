from django import forms
from .models import PersonalDetail, Home, Project, Skill, WorkHistory, Education


class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = '__all__'

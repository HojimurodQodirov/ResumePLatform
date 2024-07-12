from django import forms
from .models import Resume, WorkPlace


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'education', 'experience', 'skills']


class WorkPlaceForm(forms.ModelForm):
    class Meta:
        model = WorkPlace
        fields = ['title', 'about', 'vacation', 'email', 'phone',  'location']
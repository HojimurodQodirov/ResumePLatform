from django import forms
from .models import Resume, WorkPlace, Rating, Comment


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'education', 'experience', 'skills']


class WorkPlaceForm(forms.ModelForm):
    class Meta:
        model = WorkPlace
        fields = ['title', 'about', 'vacation', 'email', 'phone',  'location']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
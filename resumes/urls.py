from django.urls import path
from .views import ResumeListCreateView, ResumeDetailView, create_resume, view_resume

urlpatterns = [
    path('resumes/', ResumeListCreateView.as_view(), name='resume-list-create'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('create/', create_resume, name='create_resume'),
    path('<int:resume_id>/', view_resume, name='view_resume'),
]

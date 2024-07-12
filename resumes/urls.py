from django.urls import path
from .views import ResumeListCreateView, ResumeDetailView, create_resume, view_resume, create_workplace, workplace_detail, workplace_list, resume_list, home_list

urlpatterns = [
    path('create_workplace/', create_workplace, name='create_workplace'),
    path('workplaces/', workplace_list, name='workplace_list'),
    path('resumes/', resume_list, name='resume_list'),
    path('home/', home_list, name='home_list'),
    path('workplaces/<int:pk>/', workplace_detail, name='workplace_detail'),
    path('api/resumes/', ResumeListCreateView.as_view(), name='resume-list-create'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('create/resume/', create_resume, name='create_resume'),
    path('<int:resume_id>/', view_resume, name='view_resume'),
]

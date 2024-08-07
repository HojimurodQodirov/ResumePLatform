from django.urls import path
from .views import ResumeListCreateView, ResumeDetailView, create_resume, view_resume, create_workplace, \
    workplace_detail, workplace_list, resume_list, home_list, create_rating, create_comments, news_detail

urlpatterns = [
    path('workplaces/<int:pk>/', workplace_detail, name='workplace_detail'),
    path('workplaces/<int:workplace_id>/rate/', create_rating, name='create_rating'),
    path('create_workplace/', create_workplace, name='create_workplace'),
    path('workplaces/', workplace_list, name='workplace_list'),
    path('resumes/', resume_list, name='resume_list'),
    path('home/', home_list, name='home_list'),
    path('home/<int:pk>/', news_detail, name='news_detail'),
    path('api/resumes/', ResumeListCreateView.as_view(), name='resume-list-create'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('create/resume/', create_resume, name='create_resume'),
    path('<int:pk>/', view_resume, name='view_resume'),
    path('resumes/<int:resume_id>/comment/', create_comments, name='create_comment'),

]

from rest_framework import generics
from .models import Resume, News
from .serializers import ResumeSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkPlaceForm, RatingForm, CommentForm
from .models import WorkPlace


@login_required
def create_rating(request, workplace_id):
    workplace = get_object_or_404(WorkPlace, id=workplace_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.workplace = workplace
            rating.save()
            return redirect('workplace_detail', pk=workplace.id)
    else:
        form = RatingForm()
    return render(request, 'resumes/create_rating.html', {'form': form, 'workplace': workplace})


@login_required
def create_comments(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('resume_detail', pk=resume.id)
    else:
        form = CommentForm()
    return render(request, 'resumes/creating_comments.html', {'form': form, 'resume': resume})


def create_workplace(request):
    if request.method == 'POST':
        form = WorkPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workplace_list')
    else:
        form = WorkPlaceForm()
    return render(request, 'resumes/create_workplace.html', {'form': form})


def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})


def home_list(request):
    news = News.objects.all()
    return render(request, 'resumes/home.html', {'news': news})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)  # Используйте модель News вместо WorkPlace
    return render(request, 'resumes/news.html', {'news': news})


def workplace_list(request):
    workplaces = WorkPlace.objects.all()
    return render(request, 'resumes/workplace_list.html', {'workplaces': workplaces})


def workplace_detail(request, pk):
    workplace = get_object_or_404(WorkPlace, pk=pk)
    rating_form = RatingForm()
    return render(request, 'resumes/workplace_detail.html', {'workplace': workplace, 'rating_form': rating_form})


@login_required
def view_resume(request, pk):
    resume = get_object_or_404(WorkPlace, pk=pk)
    comment_form = CommentForm()
    return render(request, 'resumes/view_resume.html', {'resume': resume, 'comment_form': comment_form})


class ResumeListCreateView(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]


@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('view_resume', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'resumes/create_resume.html', {'form': form})




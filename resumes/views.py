from rest_framework import generics
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkPlaceForm
from .models import WorkPlace


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
    resumes = Resume.objects.all()
    return render(request, 'resumes/home.html', {'resumes': resumes})


def workplace_list(request):
    workplaces = WorkPlace.objects.all()
    return render(request, 'resumes/workplace_list.html', {'workplaces': workplaces})


def workplace_detail(request, pk):
    workplace = get_object_or_404(WorkPlace, pk=pk)
    return render(request, 'resumes/workplace_detail.html', {'workplace': workplace})


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


@login_required
def view_resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'resumes/view_resume.html', {'resume': resume})

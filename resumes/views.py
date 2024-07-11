from rest_framework import generics
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm


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

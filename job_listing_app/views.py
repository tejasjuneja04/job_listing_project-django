from django.shortcuts import render, redirect
from .models import Job, JobApplication
from .forms import JobForm, ApplicationForm

def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})

def upload_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JobForm()
    return render(request, 'upload_job.html', {'form': form})

def apply_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.instance.job = job
            form.save()
            return redirect('index')
    else:
        form = ApplicationForm()
    return render(request, 'apply_job.html', {'form': form})

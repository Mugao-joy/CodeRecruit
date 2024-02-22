from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from crjob_board.models import jobs
from .forms import jobform
from django.db.models import Q

# Create your views here.
def landing (request):
    return render (request, 'landing.html')
#login_required
def home(request):
    job = jobs.objects.all()

    context = {
        'jobs' : job
    }
    return render (request, 'home.html',context)

def create(request):
    form = jobform(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('crjob_board:home')

    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def submitted(request):
    return render(request, 'submitted.html')

def job_search(request):
    query = request.GET.get('q')
    if query:
        jobs = jobs.objects.filter(title__icontains=query)
    else:
        jobs= jobs.objects.all()
    return render(request, 'search_results.html', {'jobs': jobs, 'query': query})

def search_results(request):
    query = request.GET.get('q')
    if query:
        # Perform a case-insensitive search on job title or description
        jobs = jobs.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        jobs = jobs.objects.all()
    return render(request, 'search_results.html', {'jobs': jobs, 'query': query})
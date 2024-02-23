from django.shortcuts import render, redirect,get_object_or_404
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

def search_results(request):
    query = request.GET.get('q')
    if query:
        # Perform your search logic here
        jobs = jobs.objects.filter(job_title__icontains=query)  # Example query, adjust as per your model fields
        
        # Pass the search results to the template
        return render(request, 'search_results.html', {'jobs': jobs, 'query': query})
    else:
        # Handle case where no search query is provided
        return render(request, 'search_results.html', {'jobs': None, 'query': None})

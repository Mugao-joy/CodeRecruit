from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from crjob_board.models import jobs
from .forms import jobform

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
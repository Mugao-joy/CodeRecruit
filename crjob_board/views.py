from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing (request):
    return render (request, 'landing.html')
#login_required
def home(request):
    return render (request, 'home.html')
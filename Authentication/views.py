from django.shortcuts import render
from .forms import Userform

def user_register(request):
    form = Userform()

    context = {
        'form' : form
    }
    return render (request, 'register.html',context)

# Create your views here.
def user_login(request):
    return render (request, 'login.html')
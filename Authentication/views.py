from django.shortcuts import render

def user_register(request):
    return render (request, 'register.html')

# Create your views here.
def user_login(request):
    return render (request, 'login.html')
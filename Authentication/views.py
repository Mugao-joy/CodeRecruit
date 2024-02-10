from django.shortcuts import render,redirect
from .forms import Userform
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def user_register(request):

    if request.method == 'POST':
        form = Userform(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('Authentication:login')
    else:
        form = Userform()
    context = {
        'form' : form
    }
    return render (request, 'register.html',context)

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('Home:home')
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE!')
            
        else:
            return HttpResponse('ACCOUNT DOES NOT EXIST')
    return render (request, 'login.html')

#login_required
def user_logout(request):
    logout(request)
    return redirect('Home:landing')
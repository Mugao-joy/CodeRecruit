from django.shortcuts import render,redirect
from .forms import Userform

def user_register(request):

    if request.method == 'post':
        form = Userform(request.post)

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
    return render (request, 'login.html')
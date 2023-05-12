from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import forms
from .forms import createuserform
from django.contrib.auth.models import User

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username= name , email= email,password=password1)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request,'user register successfull.')
            return redirect('login')
        else:
            messages.warning(request,'invaild access..')
            return redirect('register')
    else:
        form = createuserform()
        return render(request,'register.html',{'form':form})
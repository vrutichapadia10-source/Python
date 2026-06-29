from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashbord(request):
    return render(request,'dashbord.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashbord')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def user_login(request):
    
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('dashbord')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('dashbord')
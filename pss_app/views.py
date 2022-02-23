from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def register(request):

    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegistrationForm()	
    
    return render(request, "register.html", {"form":form})

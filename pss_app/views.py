from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.views import generic, View
from pss_app.models import Post

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def feed(request):
    return render(request, "feed.html", {})

def register(request):

    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegistrationForm()	
    
    return render(request, "register.html", {"form":form})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

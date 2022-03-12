from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.views.generic import ListView
from pss_app.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.

# register a new user
def register(request):

    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegistrationForm()	
    
    return render(request, "register.html", {"form":form})

# public feed
class ImageFeedView(ListView):
    model = Post     
    template_name = 'feed_public.html'
    context_object_name = 'photos'
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    paginate_by = 30
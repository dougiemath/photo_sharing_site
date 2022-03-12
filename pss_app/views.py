from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UploadForm
from django.views.generic import ListView, DetailView, CreateView
from pss_app.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy


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

# image details page
class ImageDetailView(DetailView):
    model = Post
    template_name = 'image_detail.html'
    context_object_name = 'image'

# view image's tags
class ImageTagListView(ImageFeedView):
    
    template_name = 'taglist.html'
    
    def get_tag(self):
        return self.kwargs.get('tag')

    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context

class ImageCreateView(LoginRequiredMixin, CreateView):
    
    model = Post
    form_class = UploadForm
    template_name = 'upload_image.html'
    success_url = reverse_lazy('image:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
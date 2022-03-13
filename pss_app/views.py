from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UploadForm, CommentForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pss_app.models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

# create a new image
class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = UploadForm
    template_name = 'upload_image.html'
    success_url = reverse_lazy('image:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# check user is valid
class UserIsAuthor(UserPassesTestMixin):

    def get_photo(self):
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))
    
    def test_func(self):
        
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().author
        else:
            raise PermissionDenied('Sorry, nope!')

# update / change image
class ImageUpdateView(UserIsAuthor, UpdateView):
    template_name = 'update.html'
    model = Post
    fields = ['title', 'description', 'tags', 'status']
    success_url = reverse_lazy('image:list')

# delete image
class ImageDeleteView(UserIsAuthor, DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('image:user_feed')

#login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

#user feed page
class UserPostList(LoginRequiredMixin, ListView):

    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "user_feed.html"
    context_object_name = 'photos'
    paginate_by = 30

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

#user image page
class UserImageDetails(DetailView):
    model = Post
    template_name = 'user_image_details.html'
    context_object_name = 'image'

class AddCommentView(CreateView):

    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('image:list')


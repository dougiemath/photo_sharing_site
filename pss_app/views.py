from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.views import generic, View
# from pss_app.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



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


# class PostList(LoginRequiredMixin, generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "feed.html"
#     paginate_by = 6


# class UserPostList(LoginRequiredMixin, generic.ListView):

#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "user_feed.html"
#     paginate_by = 6

#     def get_queryset(self):

#         user = self.request.user
#         return Post.objects.filter(author=user)

# class PostDetail(View):
    
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "image_details.html",
#             {
#                 "post": post,
#             },
#         )
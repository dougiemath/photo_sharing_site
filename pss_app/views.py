from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadForm, CommentForm
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from pss_app.models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

"""
Classview to display public photostream
"""


class ImageFeedView(ListView):
    model = Post
    template_name = 'feed_public.html'
    context_object_name = 'photos'
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    paginate_by = 30

"""
Classview to display all photos that
share a tag (from clicking on a tag on the
image details page)
"""


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

"""
Classview to display more information about
each image
"""


class ImageDetailView(DetailView):

    model = Post
    template_name = 'image_detail.html'
    context_object_name = 'image'
    liked = False

    def liked(request, pk):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, id=request.POST.get('image_id'))

        if post.likes.filter(id=request.user.id).exists():
            liked = True

"""
Classview to allow users to upload
a photo to the site
"""


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = UploadForm
    template_name = 'upload_image.html'
    success_url = reverse_lazy('image:user_feed')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

"""
Classview to ensure that only the author
of the image can view their image
"""


class UserIsAuthor(UserPassesTestMixin):

    def get_photo(self):
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().author
        else:
            raise PermissionDenied('Sorry, nope!')

"""
Classview to allow users to make changes to
their images
"""


class ImageUpdateView(LoginRequiredMixin, UserIsAuthor, UpdateView):
    template_name = 'update.html'
    model = Post
    fields = ['title', 'featured_image', 'description', 'tags', 'status']

    def get_success_url(self):
        post = self.kwargs['pk']
        return reverse_lazy('image:user_image_details', kwargs={'pk': post})

"""
Classview to users to delete their images
"""


class ImageDeleteView(LoginRequiredMixin, UserIsAuthor, DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('image:user_feed')

"""
Classview to display users' personal images
"""


class UserPostList(LoginRequiredMixin, ListView):
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "user_feed.html"
    context_object_name = 'photos'
    paginate_by = 30

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

"""
Classview to display mor information on the users'
personal image
"""


class UserImageDetails(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'user_image_details.html'
    context_object_name = 'image'

"""
Classview to allow users to add a comment
"""


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        post = self.kwargs['pk']
        return reverse_lazy('image:detail', kwargs={'pk': post})

"""
Functionview to search for images by
entering a tag
"""


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(tags__name=searched, status=1)
        return render(request, 'search_results.html',
                               {'searched': searched,
                                'posts': posts})

    else:
        return render(request, 'search_results.html', {})

"""
Functionview to like images
"""


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('image_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('image:detail', args=[str(pk)]))

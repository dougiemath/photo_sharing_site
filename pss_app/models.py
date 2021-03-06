from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


STATUS = ((0, "Draft"), (1, "Published"))

"""
Images are being treated as 'post' due
to similar setup to blog
"""


class Post(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image')
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,
                                   related_name='blogpost_like',
                                   blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


"""
Comments model
"""


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, related_name='comment_author', on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

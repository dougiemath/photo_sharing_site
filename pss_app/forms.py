from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pss_app.models import Post, Comment
from allauth.account.forms import SignupForm

"""
Upload Image Form
"""
class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image','description', 'tags', 'status')

"""
Comment Form
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
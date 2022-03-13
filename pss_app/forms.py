from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pss_app.models import Post, Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        User._meta.get_field('email')._unique = True

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image','description', 'tags', 'status')


# form for adding comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

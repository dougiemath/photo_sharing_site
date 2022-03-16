from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pss_app.models import Post, Comment
from allauth.account.forms import SignupForm



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

# class MyCustomSignupForm(SignupForm):
    
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
#         exclude = ('email',)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields.pop('email')

#     def signup(self, request, user):
#         pass

#     def save(self, request):
#         user = super(MyCustomSignupForm, self).save(request)
#         return user

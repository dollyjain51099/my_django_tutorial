from django import forms
from .models import Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NameForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('Title', 'Description', 'author')

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


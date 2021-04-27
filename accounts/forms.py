from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(max_length=30)
  email = forms.EmailField(max_length=254)

  class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
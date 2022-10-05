from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# IMPORTANT --> To make the email field required, I have changed the email field's blank attribute to False of UserCreationForm.
# IMPORTANT --> Added 'form-control' class in UserCreationForm and AuthenticationForm.
class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email']
    error_messages = {
      'username' : {'required' : 'Required'},
      'email' : {'required' : 'Required'}
    }
    widgets = {
      'username' : forms.TextInput(attrs={'class':'form-control'}),
      'email' : forms.TextInput(attrs={'class':'form-control'}),
    }

class SigninForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ['username', 'password']

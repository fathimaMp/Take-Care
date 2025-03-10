from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordChangeForm):
    pass
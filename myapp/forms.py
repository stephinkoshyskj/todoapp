from django.forms import ModelForm
from django import forms
from .models import Todo

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class TodoForm(ModelForm):

    class Meta:

        model = Todo

        fields =["title"]

        widgets = {"title":forms.TextInput(attrs={"class":"form-control"})}

class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:

        model = User

        fields = ["username", "email", "password1", "password2"]

class SignInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )

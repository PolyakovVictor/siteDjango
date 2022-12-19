from dataclasses import fields
from email.mime import image
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import Product
from django.forms import ModelForm, TextInput, Textarea, ImageField, FileInput

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class RegisterUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-input'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
#         }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_input', 'placeholder': ' '}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form_input', 'type': 'password', 'placeholder': ' '}))

    class Meta:
        model = User
        fields = ['username']

        widgets = {
            'username': forms.TextInput(attrs={'class': "form_input", 'placeholder': " "}),
        }


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form_input', 'type': 'password', 'placeholder': ' '}),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form_input', 'type': 'password', 'placeholder': ' '}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': "form_input", 'placeholder': " "}),
            'first_name': forms.TextInput(attrs={'class': "form_input", 'placeholder': " "}),
            'email': forms.TextInput(attrs={'class': "form_input", 'placeholder': " "}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'image', 'description', 'price']
        widgets = {
            "name": TextInput(attrs={'class': "form_input", 'placeholder': " "}),
            "slug": TextInput(attrs={'class': "form_input", 'placeholder': " "}),
            "description": Textarea(attrs={'class': "form_input", 'placeholder': " "}),
            "price": TextInput(attrs={'class': "form_input", 'placeholder': " "}),
        }

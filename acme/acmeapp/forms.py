from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Home, About, Service

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['title', 'description', 'box_title', 'box_description', 'footer']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['about_us', 'info', 'detailed_info', 'our_job', 'job_info', 'footer']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['services', 'title', 'info', 'price', 'quote_title', 'footer']

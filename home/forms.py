from django import forms
from django.forms import (CharField, TextInput)
from allauth.account.forms import SignupForm
from .models import MyUser


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name',
        widget=TextInput(attrs={'placeholder': 'First Name','class': 'form-control'}))
    last_name = forms.CharField(max_length=30, label='Last Name',
        widget=TextInput(attrs={'placeholder': 'Last Name','class': 'form-control'}))
    business_name = forms.CharField(max_length=100, label='Business Name',
        widget=TextInput(attrs={'placeholder': 'Business Name','class': 'form-control'}))
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.business_name = self.cleaned_data['business_name']
        user.save()
        return user


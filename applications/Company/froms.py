from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company,UpdateProfileRequest
from django.forms import ModelForm


class companyRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2','is_staff']


class UpdateProfileRequestForms(forms.ModelForm):
    class Meta:
        model = UpdateProfileRequest
        fields = ['Request_update']



class CompanyForms(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['About','Company_logo','category','phone_number','address','skill']
        exclude = [
            'User'
        ]


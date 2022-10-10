from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserInfo
from django.forms import ModelForm


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2','is_staff']



class UserProfileForms(forms.ModelForm):
    class Meta:
        model = UserInfo
        #fields = '__all__'
        #fields = ['About','category','phone_number','profile_pic']
        fields = ['About','category','phone_number','address','gender','profile_pic','sccs','sschool_name','sccs_document','hschool_document','college_document','hsccs','hschool_name','dgree','college_name']
        exclude = ['user']


# class UserForms(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     address = forms.CharField(required=True,widget=forms.Textarea)
#     phone = forms.CharField(required=True)
#     profie = forms.ImageField()


#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False) #data save 
#         user.is_user = True
#         user.is_staff = True
#         user.is_active = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         user_data = User_TB.objects.create(user=user)
#         user_data.address = self.cleaned_data.get('address')
#         user_data.phone = self.cleaned_data.get('phone')
#         user_data.profile_pic = self.cleaned_data.get('profile_pic')
        
        
#         user_data.save()
#         return user


# class CompanyForms(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone = forms.CharField(required=True)
#     address = forms.CharField(required=True,widget=forms.Textarea)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_company = True
#         user.is_staff = True
#         user.is_active = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
    
#         user.save()
#         company_data = Company_table.objects.create(user=user)
#         company_data.address = self.cleaned_data.get('address')
#         company_data.save()
#         return user


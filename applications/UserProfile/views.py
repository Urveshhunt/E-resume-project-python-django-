from msilib.schema import ListView
from re import I
from . import forms,models
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister,UserProfileForms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import UserInfo
from django.views import View
from django.db.models import Q
# Create your views here.

@login_required(login_url='Homepage')
def searchEmp(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        object_list = UserInfo.objects.get(
            Q(phone_number__icontains=query) | Q(About__icontains=query)
        )
    #return render(request,"UserProfile/searchemp.html",{'object_list':object_list})
    return render(request,"UserProfile/searchemp.html",{'object_list':object_list})

class PasswordUpdate(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('Homepage')


def Userregisterview(request):
    userdata = UserRegister(request.POST)
    if userdata.is_valid():
        userdata.save()
        return redirect('Homepage')
    contenxt = {
        'userdata':userdata
    }
    return render(request,"register.html",contenxt)

@login_required(login_url='Homepage')
def UserProfile(request):
    try:
        user = request.user.userinfo
        formData = UserProfileForms(instance=user)
        if request.method == "POST":
            forms = UserProfileForms(request.POST,request.FILES,instance=request.user.userinfo)
            if forms.is_valid():
                forms.save()
                return redirect('About_us')
            else:
                return render(request, 'UserProfile/UserProfileinfo.html',{'forms':forms})        
        context = {
            'formData':formData
        }
    except:     
        return HttpResponse('plz connect to admin')
    return render(request, 'UserProfile/UserProfileinfo.html',context)



@login_required(login_url='Homepage')
def UpdateUserProfile(request):
    #formData = UserProfileForms()
    return render(request, 'UserProfile/UserProfile.html')


'''
@login_required(login_url='Homepage')
def UserProfile(request,pk):
    DataTr = UserInfo.objects.get(id=pk)
    userData = User.objects.get(id=DataTr.user_id)
    U = UserRegister(instance=userData)
    c = UserProfileForms(request.FILES,instance=DataTr)
    mydict = {'U':U,'c':c}
    if request.method == "POST":
        U = UserRegister(request,instance=userData)
        c = UserProfileForms(request.FILES,instance=DataTr)
        if U.is_valid() and c.is_valid():
            user = U.save()

    return render(request, 'UserProfile/UserProfile.html',context = mydict)
'''

def Homepage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_staff and user.is_active:
                request.session['user'] = username
                login(request, user)
                return redirect('dashbord')
            else:
                request.session['user'] = username
                login(request,user)
                return redirect('dashbord')
        else:
            return render(request, "login.html", {'msg': "Invalid Username Or Password"})
    return render(request, "login.html")


def userLogout(request):
    logout(request)
    return redirect('Homepage') 

@login_required(login_url='Homepage')
def dashbord(request):
    return render(request, "UserProfile/home.html")

@login_required(login_url='Homepage')
def About_us(request):
    about_data = UserInfo.objects.filter(user = request.user)
    return render(request, "UserProfile/about.html",{'about_data':about_data})

@login_required(login_url='Homepage')
def Resume(request):
    user = request.user
    resume_data = UserInfo.objects.filter(user = request.user)
    return render(request, "UserProfile/resume.html",{'resume_data':resume_data})

@login_required(login_url='Homepage')
def Porfolio(request):
    return render(request, "UserProfile/porfolio.html")

@login_required(login_url='Homepage')
def Blog(request):
    return render(request, "UserProfile/blog.html")

@login_required(login_url='Homepage')
def Contact(request):
    return render(request, "UserProfile/contact.html")


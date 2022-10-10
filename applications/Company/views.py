from django.shortcuts import render,redirect
from django.db.models import Q
from UserProfile.models import UserInfo 
from django.contrib.auth.models import User
from .models import Company
from .froms import companyRegister,CompanyForms,UpdateProfileRequestForms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='Homepage')
def searchemp(request):
    if request.method == "GET":
        query = request.GET.get('q')
        results = UserInfo.objects.filter(Q(phone_number__icontains=query) )
    return render(request,"UserProfile/searchemp.html")


@login_required(login_url='Homepage')
def RequestUpdateProfileCompany(request):
    data = UpdateProfileRequestForms(request.POST)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect('CompanyProfile')
        else:
            print("error")
    return render(request,"UserProfile/RequestUpdateProfileCompany.html",{'data':data})

@login_required(login_url='Homepage')
def CompanyProfile(request):
    user = request.user.company
    formdata = CompanyForms(instance=user)
    if request.method == "POST":
        forms = CompanyForms(request.POST,request.FILES,instance=request.user.company)
        if forms.is_valid():
            forms.save()
            return redirect('CompanyProfile')
        else:
            return render(request, 'UserProfile/companyprofile.html',{'forms':forms})
    context = {
        'formdata':formdata
    }
    return render(request, 'UserProfile/companyprofile.html',context)



@login_required(login_url='Homepage')
def UpdateCompanyProfile(request,id):
    UserProfileData = CompanyForms(instance=request.user)
    return render(request, 'UserProfile/companyprofileupdate.html',{'UserProfileData':UserProfileData})



 
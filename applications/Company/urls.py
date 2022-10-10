from django.urls import path
from . import views

urlpatterns = [
    path('',views.searchemp,name="searchemp"),
    path('CompanyProfile/',views.CompanyProfile,name="CompanyProfile"),
    path('UpdateCompanyProfile/<int:id>',views.UpdateCompanyProfile,name="UpdateCompanyProfile"),
    path('RequestUpdateProfileCompany/',views.RequestUpdateProfileCompany,name="RequestUpdateProfileCompany"),
    
]

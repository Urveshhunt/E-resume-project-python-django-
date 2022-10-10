import imp
from re import template
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.Homepage, name="Homepage"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('About_us/', views.About_us, name="About_us"),
    path('Resume/', views.Resume, name="Resume"),
    path('Porfolio/', views.Porfolio, name="Porfolio"),
    path('Blog/', views.Blog, name="Blog"),
    path('Contact/', views.Contact, name="Contact"),
    path('Userregisterview/',views.Userregisterview,name="Userregisterview"),
    path('userLogout/',views.userLogout,name="userLogout"),
    path('changepassword/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('Homepage'),template_name='updatepassword.html'),name="changepassword"),
    path('UserProfile/',views.UserProfile,name="UserProfile"),
    path('UpdateUserProfile/',views.UpdateUserProfile,name="UpdateUserProfile"),
    path('searchEmp/',views.searchEmp,name="searchEmp")
]

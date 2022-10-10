from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf.urls.static import static
# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    About = models.TextField()
    category = models.ForeignKey("category.Category",on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    gender = models.CharField(max_length=1,
    choices=(
        ('M',"Male"),
        ('F',"Female"),
    )
    )
    #skill = models.ManyToManyField("skill.Skill")
    profile_pic = models.ImageField(upload_to="image/userprofil/")
    sccs = models.CharField(max_length=30)
    sccs_document = models.FileField(upload_to="image/userprofil/")
    sschool_name = models.CharField(max_length=30)
    hsccs = models.CharField(max_length=30)
    hschool_name = models.CharField(max_length=30)
    hschool_document = models.FileField(upload_to="image/userprofil/")
    dgree = models.CharField(max_length=30)
    college_name = models.CharField(max_length=30)
    college_document = models.FileField(upload_to="image/userprofil/")
    
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

    @property
    def get_avatar(self):
        return self.profile_pic.url if self.profile_pic else static('assets/img/team/default-profile-picture.png')
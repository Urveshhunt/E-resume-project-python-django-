from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


# Create your models here.

class Company(models.Model):
    User = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    About = models.TextField()
    Company_logo = models.ImageField(upload_to="image/companyLogo/")
    category = models.ForeignKey("category.Category",on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    skill = models.ForeignKey("skill.Skill",on_delete=models.CASCADE)
    

class UpdateProfileRequest(models.Model):
    Request_update = models.TextField()
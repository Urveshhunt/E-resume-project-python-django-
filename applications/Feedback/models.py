from django.db import models
# Create your models here.



class Feedback(models.Model):
    Username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)
    msg = models.TextField()
    
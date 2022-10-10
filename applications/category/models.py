from django.db import models

# Create your models here.

class Category(models.Model):
    cate_name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.cate_name
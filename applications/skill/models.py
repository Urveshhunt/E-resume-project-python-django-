from django.db import models

# Create your models here.
class Skill(models.Model):
    programming_languages = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.programming_languages
    
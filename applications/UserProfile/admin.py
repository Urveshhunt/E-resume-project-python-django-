from django.contrib import admin
from .models import UserInfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(UserInfo)

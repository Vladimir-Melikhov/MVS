from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Mvs_User


admin.site.register(Mvs_User, UserAdmin)
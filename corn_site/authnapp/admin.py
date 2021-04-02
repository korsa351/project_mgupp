from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import OfficeUser

class OfficeUserAdmin(UserAdmin):
    pass

admin.site.register(OfficeUser, OfficeUserAdmin)
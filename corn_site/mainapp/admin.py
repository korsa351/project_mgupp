from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


admin.site.register(RefEventTypes)
admin.site.register(Customers)
admin.site.register(Events)
admin.site.register(EventRegistrations)
admin.site.register(EventReservartions)
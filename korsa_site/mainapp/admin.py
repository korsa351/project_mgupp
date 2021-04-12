from django.contrib import admin
from .models import Addresses, Gymnasts, Meets, University, University_Meet_Participation


admin.site.register(Addresses)
admin.site.register(Gymnasts)
admin.site.register(Meets)
admin.site.register(University)
admin.site.register(University_Meet_Participation)
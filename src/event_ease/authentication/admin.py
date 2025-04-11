from django.contrib import admin

from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'phone', 'date_of_birth', 'profile_image']

admin.site.register(Customer, CustomerAdmin)

from django.contrib import admin

from .models import *


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'feature_image']

admin.site.register(Feature, FeatureAdmin)

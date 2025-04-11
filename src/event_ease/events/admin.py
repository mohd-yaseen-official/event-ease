from django.contrib import admin

from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date_and_time', 'venue', 'type', 'customer', 'is_deleted']

admin.site.register(Event, EventAdmin)


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(EventType, EventTypeAdmin)


class DummyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(Dummy, DummyAdmin)

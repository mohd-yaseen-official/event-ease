from django.urls import path

from .views import *


app_name = 'events'

urlpatterns = [
    
    path('add/', add_event, name='add_event'),

    path('my-events/', my_events, name='my_events'),

    path("<int:id>", view_event, name="view_event"),

    path('edit/<int:id>', edit_event, name='edit_event'),
    
    path('delete/<int:id>', delete_event, name='delete_event')
]
from django import forms

from .models import *


class EventForm(forms.ModelForm):

    event_type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Event Type')

    class Meta:
        model = Event
        
        fields = ['title', 'description', 'date_and_time', 'venue',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.Textarea(attrs={'class': 'form-control'}),

            'date_and_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),

            'venue': forms.TextInput(attrs={'class': 'form-control'}),
        }
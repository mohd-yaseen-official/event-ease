from datetime import date

from django import forms
from django.contrib.auth.models import User

from .models import Customer


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [ 'first_name', 'last_name', 'email','username', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            'username': forms.TextInput(attrs={'class': 'form-control'}),

            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter A Strong Password'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = [ 'phone', 'date_of_birth', 'address','profile_image']

        widgets = {
            'phone': forms.widgets.NumberInput(attrs={'type': 'tel', 'class': 'form-control'}),

            'date_of_birth': forms.widgets.DateInput(attrs={'type': 'date', 'max': date.today(), 'class': 'form-control'}),

            'address': forms.widgets.Textarea(attrs={'class': 'form-control'}),
            
            'profile_image': forms.widgets.FileInput(attrs={'class': 'form-control'}),
        }
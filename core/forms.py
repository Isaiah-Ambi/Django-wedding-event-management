from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Guest, Wedding, Venue

import datetime

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email', 'phone', 'status']

class GuestUpdateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['status']

class WeddingForm(forms.ModelForm):
    class Meta:
        model = Wedding
        fields = ['title', 'description', 'date', 'time', 'venue']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',  # HTML5 date picker
                    'class': 'form-control',
                    'min': datetime.date.today().strftime('%Y-%m-%d'),
                    'placeholder': 'Select a date'
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',  # HTML5 time picker
                    'class': 'form-control',
                    'placeholder': 'Select a time'
                }
            ),
        }

class WeddingUpdateForm(forms.ModelForm):
    class Meta:
        model = Wedding
        fields = ['title', 'description', 'date', 'time', 'venue']

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'photo', 'address', 'website']
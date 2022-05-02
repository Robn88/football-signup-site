from django import forms
from .models import Registration


'''
This is the registration form. It draws on
the Registration model, and has 3 fields.
'''


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ("ball", "bibs", "guest",)

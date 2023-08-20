from django import forms
from .models import Enseignant


class EnseignantLoginForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['email', 'password']
        widgets = {'password': forms.PasswordInput()}

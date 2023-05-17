# Django
from django import forms

# Combinational Motifs
from core.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
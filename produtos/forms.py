from django import forms
from .models import ComprarModel

class ComprarForms(forms.ModelForm):
    class Meta:
        model = ComprarModel
        fields = '__all__'

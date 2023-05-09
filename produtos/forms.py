from django import forms
from .models import ComprarModel
from .models import ProdutoModel

class ComprarForms(forms.ModelForm):
    class Meta:
        model = ComprarModel
        fields = '__all__'

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = ProdutoModel
        fields = '__all__'

from django import forms
from django.contrib.auth.models import User
class UsuarioForms(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),

    )
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),

    )
    class Meta:
        model = User
        fields = ('username','email','password','password2',)

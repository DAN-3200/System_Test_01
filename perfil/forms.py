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

    def clean(self):
        username_form = self.cleaned_data.get('username')
        password_form = self.cleaned_data.get('password')
        email_form = self.cleaned_data.get('email')
        password2_form = self.cleaned_data.get('password2')

        validation_error_msgs = {}

        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'E-mail já existe'
        error_msg_password_match = 'As duas senhas não conferem'
        error_msg_required_field = 'Este campo é obrigatório.'
        error_msg_len = 'Este campo precisa ter 8.'

        usuario_banco = User.objects.filter(username=username_form).first()
        email_banco = User.objects.filter(email=email_form).first()

        if usuario_banco:
            validation_error_msgs['username'] = error_msg_user_exists

        if email_banco:
            validation_error_msgs['email'] = error_msg_email_exists

        if not email_form:
            validation_error_msgs['email'] = error_msg_required_field

        if len(password_form) < 8:
            validation_error_msgs['password'] = error_msg_len

        if not password_form:
            validation_error_msgs['password'] = error_msg_required_field

        if not password2_form:
            validation_error_msgs['password2'] = error_msg_required_field

        if password_form != password2_form:
            validation_error_msgs['password'] = error_msg_password_match
            validation_error_msgs['password2'] = error_msg_password_match

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))

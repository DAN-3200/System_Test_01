from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

class TesteUsuario(TestCase):

    def setUp(self):
        User.objects.create_user(username='Thiago456', password='g456h123')
        self.cliente = Client()
    def test_usuario_criado(self):
        usuario = User.objects.get(username='Thiago456')
        self.assertEquals(usuario.username, 'Thiago456')

    def test_login(self):
        # Simular o login
        response = self.cliente.post(reverse('perfil:login'), {'username': 'Thiago456', 'password': 'g456h123'})
        self.assertRedirects(response, reverse('produtos:home'))

    def test_deletar_usuario(self):
        usuario = User.objects.get(username='Thiago456')
        usuario.delete()
        self.assertFalse(User.objects.filter(username='Thiago456').exists())



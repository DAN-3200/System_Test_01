from django.test import TestCase
from django.contrib.auth.models import User
from .models import ProdutoModel
from .models import ComprarModel
class TestProduto(TestCase):
    def setUp(self):
        ProdutoModel.objects.create(prod_nome='TV plana')
        User.objects.create_user(username='Thiago456', password='g456h123')
    def test_produto_criado(self):
        produto = ProdutoModel.objects.get(prod_nome='TV plana')
        self.assertEquals(produto.prod_nome, 'TV plana')

    def test_pcomprar_usuario(self):
        produto = ProdutoModel.objects.filter(prod_nome='TV plana')
        usuario = User.objects.filter(username='Thiago456')
        comprar = ComprarModel.objects.create(comp_produto_fk=produto[0],comp_usuario_fk=usuario[0],comp_quantidade=4)

    def test_deletar_usuario(self):
        produto = ProdutoModel.objects.get(prod_nome='TV plana')
        produto.delete()
        self.assertFalse(ProdutoModel.objects.filter(prod_nome='TV plana').exists())


# Create your tests here.

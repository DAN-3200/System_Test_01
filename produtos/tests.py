from django.test import TestCase
from .models import ProdutoModel
class TestProduto(TestCase):
    def setUp(self):
        ProdutoModel.objects.create(prod_nome='TV plana')
    def test_produto_criado(self):
        produto = ProdutoModel.objects.get(prod_nome='TV plana')
        self.assertEquals(produto.prod_nome, 'TV plana')

    def test_deletar_usuario(self):
        produto = ProdutoModel.objects.get(prod_nome='TV plana')
        produto.delete()
        self.assertFalse(ProdutoModel.objects.filter(prod_nome='TV plana').exists())

# Create your tests here.

from django.db import models

class CategoriaModel(models.Model):
    cat_codigo = models.BigAutoField(primary_key=True)
    cat_nome = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.cat_nome

class ProdutoModel(models.Model):
    prod_codigo = models.BigAutoField(primary_key=True)
    prod_nome = models.CharField(max_length=30, null=True)
    prod_estoque = models.PositiveIntegerField(null=True)
    prod_categoria_fk = models.ForeignKey(CategoriaModel, null=True, on_delete=models.DO_NOTHING)
    prod_preco = models.FloatField(null=True)
    prod_foto = models.ImageField(null=True, blank=True)
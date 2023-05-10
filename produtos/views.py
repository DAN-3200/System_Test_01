from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.db.models import Q
from django.contrib import messages
from .forms import ComprarForms
from . import models
from django.contrib.auth.models import User
class Homepage(ListView):
    model = models.ProdutoModel
    template_name = 'produtos/home.html'
    context_object_name = 'produtos'
    paginate_by = 12

class Busca(Homepage):
    def get_queryset(self, *args, **kwargs):
        nome = self.request.GET.get('nome')
        qs = super().get_queryset(*args, **kwargs)
        if not nome:
            return qs
        qs = qs.filter(
            Q(prod_nome__icontains=nome)
        )
        return qs
class DetalheProduto(DetailView):
    model = models.ProdutoModel
    template_name = 'produtos/detalhe.html'
    context_object_name = 'produto'
    pk_url_kwarg = 'prod_codigo'

class Comprar(DetalheProduto, View):

    def setup(self, *args, **kwargs):
        super().setup( *args, **kwargs)
        self.produto_db = get_object_or_404(models.ProdutoModel, prod_codigo=self.kwargs.get('prod_codigo'))
        self.produto = {
            'produto':self.produto_db,
            'comprar': ComprarForms(
                data=self.request.POST or None
            )
        }
        self.comprar = self.produto['comprar']
        self.produto_banco = self.produto['produto']
        self.page = render(self.request, self.template_name,self.produto)
    def get(self,*args, **kwargs):
        return self.page
    def post(self,*args, **kwargs):
        compra_quantidade = self.request.POST.get('comp_quantidade')
        comprar_usuario = self.comprar.save(commit=False)
        usuario = get_object_or_404(User, username=self.request.user)
        comprar_usuario.comp_usuario_fk = usuario
        comprar_usuario.comp_produto_fk = self.produto_db
        comprar_usuario.comp_quantidade = int(compra_quantidade)
        comprar_usuario.save()

        print(self.produto_banco.prod_estoque)
        self.produto_banco.prod_estoque -= int(compra_quantidade)
        self.produto_banco.save()

        messages.success(
            self.request,
            "Compra feita com sucesso"
        )

        return redirect('produtos:home')
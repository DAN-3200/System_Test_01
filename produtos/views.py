from django.shortcuts import render
from django.views.generic.list import ListView
from . import models
class Homepage(ListView):
    model = models.ProdutoModel
    template_name = 'produtos/home.html'
    context_object_name = 'produtos'
    paginate_by = 12
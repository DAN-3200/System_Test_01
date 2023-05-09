from django.urls import path
from . import views
app_name = 'produtos'
urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('<prod_codigo>', views.Comprar.as_view(), name='detalhe'),
    path('busca/', views.Busca.as_view(), name='buscar')
]
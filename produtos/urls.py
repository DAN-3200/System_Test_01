from django.urls import path
from . import views
app_name = 'produtos'
urlpatterns = [
    path('', views.Homepage.as_view(), name='home')
]
from django.urls import path
from .views import ListaFuncionarioView, FuncionarioCreateView

urlpatterns = [
    path('', ListaFuncionarioView.as_view(), name='funcionario.index'),
    path('novo/', FuncionarioCreateView.as_view(), name='funcionario.novo')
]

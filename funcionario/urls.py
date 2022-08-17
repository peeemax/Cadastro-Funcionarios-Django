from django.urls import path
from .views import ListaFuncionarioView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView

urlpatterns = [
    path('', ListaFuncionarioView.as_view(), name='funcionario.index'),
    path('novo/', FuncionarioCreateView.as_view(), name='funcionario.novo'),
    path('atualizar/<int:pk>', FuncionarioUpdateView.as_view(), name='funcionario.atualizar'),
    path('deletar/<int:pk>', FuncionarioDeleteView.as_view(), name='funcionario.deletar')
]

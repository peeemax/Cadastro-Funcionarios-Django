from django.urls import path
from .views import ListaFuncionarioView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView
from . import views

urlpatterns = [
    path('', ListaFuncionarioView.as_view(), name='funcionario.index'),
    path('novo/', FuncionarioCreateView.as_view(), name='funcionario.novo'),
    path('<int:pk>/atualizar', FuncionarioUpdateView.as_view(), name='funcionario.atualizar'),
    path('<int:pk>/deletar', FuncionarioDeleteView.as_view(), name='funcionario.deletar'),
    path('<int:pk_funcionario>/contatos', 
         views.contatos, name='funcionario.contatos'),
    path('<int:pk_funcionario>/contato/novo/', 
         views.contato_novo, name='funcionario.novo'),
    path('<int:pk_funcionario>/contato/<int:pk>/atualizar/', 
         views.contato_atualizar, name='funcionario.atualizar'),
    path('<int:pk_funcionario>/contato/<int:pk>/deletar/', 
         views.contato_deletar, name='funcionario.deletar')
]

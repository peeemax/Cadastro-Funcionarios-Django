from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListaFuncionarioView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView
from . import views

urlpatterns = [
    path('', login_required(ListaFuncionarioView.as_view()), name='funcionario.index'),
    path('novo/', login_required(FuncionarioCreateView.as_view()), name='funcionario.novo'),
    path('<int:pk>/atualizar', login_required(FuncionarioUpdateView.as_view()), name='funcionario.atualizar'),
    path('<int:pk>/deletar', login_required(FuncionarioDeleteView.as_view()), name='funcionario.deletar'),
    path('<int:pk_funcionario>/contatos', 
         login_required(views.contatos), name='funcionario.contatos'),
    path('<int:pk_funcionario>/contato/novo/', 
         login_required(views.contato_novo), name='funcionario.novo'),
    path('<int:pk_funcionario>/contato/<int:pk>/atualizar/', 
         login_required(views.contato_atualizar), name='funcionario.atualizar'),
    path('<int:pk_funcionario>/contato/<int:pk>/deletar/', 
         login_required(views.contato_deletar), name='funcionario.deletar')
]

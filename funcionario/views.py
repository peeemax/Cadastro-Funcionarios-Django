from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Funcionario
from .forms import FuncionarioForm


class ListaFuncionarioView(ListView):
    model = Funcionario
    queryset = Funcionario.objects.all().order_by('nome_completo')  # chamada no banco de dados e ordena a visualização


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = '/funcionarios/'

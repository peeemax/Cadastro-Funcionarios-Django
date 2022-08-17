from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Funcionario
from .forms import FuncionarioForm


class ListaFuncionarioView(ListView):
    model = Funcionario
    queryset = Funcionario.objects.all().order_by('nome_completo')  # chamada no banco de dados e ordena a visualização
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None
        
        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        return queryset


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = '/funcionarios/'


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = '/funcionarios/'
    

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = '/funcionarios/'
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Funcionario, Contato
from .forms import FuncionarioForm, ContatoForm


class ListaFuncionarioView(ListView):
    model = Funcionario
    queryset = Funcionario.objects.all().order_by('nome_completo')  # chamada no banco de dados e ordena a visualização
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        filtro_nome = self.request.GET.get('nome') or None
        
        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        return queryset


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = '/funcionarios/'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = '/funcionarios/'
    

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = '/funcionarios/'


def contatos(request, pk_funcionario):
    contatos = Contato.objects.filter(funcionario=pk_funcionario)
    return render(request, 'contato/contato_list.html', {'contatos': contatos, 'pk_funcionario': pk_funcionario})
    
    
def contato_novo(request, pk_funcionario):
    form = ContatoForm()
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.funcionario_id = pk_funcionario;
            contato.save()
            return redirect(reverse('funcionario.contatos', args=[pk_funcionario]))
        
    return render(request, 'contato/contato_form.html', {'form': form})


def contato_atualizar(request, pk_funcionario, pk):
    contato = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(instance=contato)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect(reverse('funcionario.contatos', args=[pk_funcionario]))
        
    return render(request, 'contato/contato_form.html', {'form': form})
 
 
def contato_deletar(request, pk_funcionario, pk):
    contato = get_object_or_404(Contato, pk=pk)
    contato.delete()
    return redirect(reverse('funcionario.contatos', args=[pk_funcionario]))

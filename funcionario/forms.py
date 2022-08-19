from django.forms import ModelForm
from django import forms
from .models import Contato, Funcionario


class FuncionarioForm(forms.ModelForm):
        data_nascimento = forms.DateField(
                widget=forms.TextInput(
                        attrs={"type": "date"}
                )
        )
        class Meta:
                model = Funcionario
                fields = ['nome_completo', 'cpf', 'data_nascimento', 'cargo', 'ativa']


class ContatoForm(forms.ModelForm):
        class Meta:
                model = Contato
                fields = ['nome', 'email', 'telefone']
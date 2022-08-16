from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        models = Funcionario
        fields = ['nome_completo', 'cpf', 'data_nascimento', 'cargo', 'ativa']

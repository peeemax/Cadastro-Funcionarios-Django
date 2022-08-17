from django import forms
from django.forms import fields, models
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
        data_nascimento = forms.DateField(
                widget=forms.TextInput(
                        attrs={"type": "date"}
                )
        )
        class Meta:
                model = Funcionario
                fields = ['nome_completo', 'cpf', 'data_nascimento', 'cargo', 'ativa']

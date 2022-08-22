from rest_framework import serializers
from funcionario.models import Contato, Funcionario


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']


class FuncionarioSerializer(serializers.ModelSerializer):
    contatos = ContatoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Funcionario
        fields = ['nome_completo', 'cpf', 'data_nascimento', 'cargo', 'ativa', 'contatos']
        
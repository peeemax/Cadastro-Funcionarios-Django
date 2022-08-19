import email
from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=256)
    cpf = models.IntegerField()
    data_nascimento = models.DateField(null=True)
    cargo = models.CharField(max_length=256)
    ativa = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome_completo


class Contato(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nome
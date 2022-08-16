from django.db import models


class Funcionario(models.Model):
    objects = None
    nome_completo = models.CharField(max_length=256)
    cpf = models.IntegerField()
    data_nascimento = models.DateField(null=True)
    cargo = models.CharField(max_length=256)
    ativa = models.BooleanField(default=True)

    def __str__(self) -> str:
        return super().__str__()


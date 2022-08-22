from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import FuncionarioSerializer

from funcionario.models import Funcionario


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('nome_completo')
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        funcionarios = super().get_queryset()
        funcionarios = funcionarios.filter(usuario=self.request.user)
        return funcionarios
    


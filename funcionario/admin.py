from django.contrib import admin

from funcionario.models import Contato, Funcionario


@admin.action(description='Ativar todos os funcionários')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)
    
    
@admin.action(description='Desativar todos os funcionários')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'cargo',
        'ativa'
    ]
    list_filter = [
        'ativa',
        'data_nascimento'
    ]
    search_fields = [
        'nome_completo',
        'cargo'
    ]
    actions = [
        ativar_todos,
        desativar_todos
    ]


admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Contato)

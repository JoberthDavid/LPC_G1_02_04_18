from django.contrib import admin
from .models import Status, Chamado, Categoria, Departamento, Funcionario, Atendimento

# Register your models here.
admin.site.register(Status)
admin.site.register(Chamado)
admin.site.register(Categoria)
admin.site.register(Departamento)
admin.site.register(Funcionario)
admin.site.register(Atendimento)
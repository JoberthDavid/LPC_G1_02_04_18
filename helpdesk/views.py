from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Status, Chamado, Categoria, Departamento, Funcionario, Atendimento

def index(request):
	status=["Aberto", "Em atendimento", "Concluído", "Cancelado"]
	chamados=["Paulo", "David", "Alberto", "Geraldo"]
	categoria=["Cat1", "Cat2"]
	departamento=["dep1", "dep2"]
	funcionario=["Alfredo", "Carlos"]
	return render(request, 'chamados.html')

def detalhes(request, chamado_id):
	return HttpResponse(str(chamado_id))

def chamados(request):
	chamados=Chamado.objects.all()
	return render(request, 'chamados.html', context={"Chamados":chamados})
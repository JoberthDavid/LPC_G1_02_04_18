from django.db import models

# Create your models here.
class Status(models.Model):
	nome=models.CharField('nome', max_length=15)

	def __str__(self):
		return "Status: "+self.nome

class Chamado(models.Model):
	titulo=models.TextField()
	descricao=models.TextField()
	telefone=models.CharField('telefone', max_length=11, null=False)
	dataAbertura=models.DateTimeField(blank=False, null=False)
	funcionario=models.ForeignKey(Funcionario)
	status=models.ForeignKey(Status)

	def __str__(self):
		return "Chamado: "+self.titulo

class Categoria(models.Model):
	nome=models.CharField('nome', max_length=15)
	chamado=models.ManyToMany(Chamado)

	def __str__(self):
		return "Categoria: "+self.nome

class Departamento(models.Model):
	nome=models.CharField('nome', max_length=15)

	def __str__(self):
		return "Departamento: "+self.nome

class Funcionario(models.Model):
	nome=models.CharField('nome', max_length=25)
	departamento=models.ForeignKey(Departamento)

	def __str__(self):
		return "Funcionário: "+self.nome

class Atendimento(models.Model):
	descricao=models.TextField()
	funcionario=models.ForeignKey(Funcionario)
	chamado=models.ForeignKey(Chamado)

	def __str__(self):
		return "Atendimento: "+descricao+"Funcionário: "+funcionario


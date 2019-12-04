# Create your models here.
from django.db import models

class Turma(models.Model):
    professor =  models.ForeignKey('Professor',on_delete=models.PROTECT)
    aluno = models.ManyToManyField('Aluno')
    disciplina = models.CharField("Disciplina",max_length=50)
    plano_ensino = models.TextField("Plano de ensino", max_length= 2000)


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField('Matricula',max_length=11)
    nota = models.DecimalField(max_digits=4,default=0,decimal_places=2)
    
    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField("Nome",max_length=50)
    email = models.EmailField("Email do professor",max_length=50)

    def __str__(self):
        return self.nome

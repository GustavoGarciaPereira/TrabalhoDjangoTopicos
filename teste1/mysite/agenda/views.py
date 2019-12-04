from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from .models import Aluno,Professor, Turma

class TurmaCreate(CreateView):
    model = Turma
    template_name = 'turma/turma_form.html'
    fields = ['professor','aluno','disciplina','plano_ensino']

    success_url = "listar_turma"

class TurmaList(ListView):
    model = Turma
    template_name = "turma/turma_list.html"

class AlunoCreate(CreateView):
    model = Aluno
    template_name = 'aluno/aluno_form.html'
    fields = ['nome','matricula','nota']

    success_url = "listar_aluno"

class AlunoList(ListView):
    model = Aluno
    template_name = "aluno/aluno_list.html"

class ProfessorCreate(CreateView):
    model = Professor
    template_name = 'professor/professor_form.html'
    fields = ['nome','email']

    success_url = "listar_professor"

class ProfessorList(ListView):
    model = Professor
    template_name = "professor/professor_list.html"
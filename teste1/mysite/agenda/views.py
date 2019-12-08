from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView

from django.contrib import messages

from .models import Aluno,Professor, Turma
from django.urls import reverse,reverse_lazy


class Home(TemplateView):
    template_name = "home/home.html"



class TurmaCreate(CreateView):
    model = Turma
    template_name = 'turma/turma_form.html'
    fields = ['professor','aluno','disciplina','plano_ensino']

    success_url = "listar_turma"

class TurmaList(ListView):
    model = Turma
    template_name = "turma/turma_list.html"


class TurmaUpdate(UpdateView):
    model = Turma
    template_name = 'turma/turma_form.html'
    fields = ['professor','aluno','disciplina','plano_ensino']

    success_url = "listar_turma"


class TurmaDelete(DeleteView):
    model = Professor
    template_name = 'truma/confirm_delete.html'
    success_url = reverse_lazy('listar_professor')

##----------------------------------------------------


class AlunoCreate(CreateView):
    model = Aluno
    template_name = 'aluno/aluno_form.html'
    fields = ['nome','matricula','nota']

    success_url = "listar_aluno"

class AlunoList(ListView):
    model = Aluno
    template_name = "aluno/aluno_list.html"

class AlunoUpdate(UpdateView):
    model = Aluno
    template_name = 'aluno/aluno_form.html'
    fields = ['nome','matricula','nota']

    success_url = "listar_aluno"

class AlunoDelete(DeleteView):
    model = Professor
    template_name = 'aluno/confirm_delete.html'
    success_url = reverse_lazy('listar_professor')


#--------------------------------------------------------

class ProfessorCreate(CreateView):
    model = Professor
    template_name = 'professor/professor_form.html'
    fields = ['nome','email']

    success_url = "listar_professor"

class ProfessorList(ListView):
    model = Professor
    template_name = "professor/professor_list.html"

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['nome','email']
    template_name = 'professor/professor_form.html'
    def get_success_url(self):
        return reverse('listar_professor')

class ProfessorDelete(DeleteView):
    model = Professor
    template_name = 'professor/confirm_delete.html'
    success_url = reverse_lazy('listar_professor')
    

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .views import AlunoCreate,AlunoList,ProfessorCreate,ProfessorList,TurmaCreate,TurmaList
urlpatterns = [
    path('cadastrar_aluno', AlunoCreate.as_view(), name='cadastrar_Aluno'),
    path('listar_aluno', AlunoList.as_view(), name='listar_Aluno'),
    path('cadastrar_professor', ProfessorCreate.as_view(), name='cadastrar_professor'),
    path('listar_professor', ProfessorList.as_view(), name='listar_Professor'),
    path('cadastrar_turma', TurmaCreate.as_view(), name='cadastrar_turma'),
    path('listar_turma', TurmaList.as_view(), name='listar_turma'),
    
]

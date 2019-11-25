from django.db import models

# Create your models here.
from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    nota = models.DecimalField(max_digits=4,default=0,decimal_places=2)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nome
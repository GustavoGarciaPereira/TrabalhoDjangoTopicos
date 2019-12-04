# Generated by Django 2.1.2 on 2019-12-02 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=50, verbose_name='Email do professor')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=50, verbose_name='Disciplina')),
                ('plano_ensino', models.TextField(max_length=2000, verbose_name='Plano de ensino')),
                ('aluno', models.ManyToManyField(to='agenda.Aluno')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.Professor')),
            ],
        ),
    ]

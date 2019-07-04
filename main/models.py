from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class TipoPerfil(models.Model):

    descricao = models.CharField(max_length=60)

    def __str__(self):
        return self.descricao


class Curso(models.Model):

    NIVEL_CHOICES = (
        ('EM','Ensino Médio'),
        ('ET', 'Ensino Técnico'),
        ('ES', 'Ensino Superior'),
    )

    TIPO_CURSO_CHOICES = (
        ('B', 'Bacharelado'),
        ('T', 'Tecnologia'),
        ('L','Licenciatura')
    )

    descricao = models.CharField(max_length=150)
    data_criacao = models.DateField()
    nivel = models.CharField(max_length=2, choices=NIVEL_CHOICES)
    tipo = models.CharField(max_length=1, choices=TIPO_CURSO_CHOICES, blank=True, null=True)
    semestre = models.IntegerField()

    def __str__(self):
        return self.descricao


class Perfil(models.Model):

    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro'),
    )

    usuario = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, related_name='perfil')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    contato = models.CharField(max_length=11, blank=True, null=True)
    tipo_perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE, related_name='perfil')

    def __str__(self):
        return self.usuario.__str__()


class Area(models.Model):

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Item(models.Model):

    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao


class Questionario(models.Model):

    descricao = models.CharField(max_length=150)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='questionario')
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='questionario')
    recomendacoes = models.CharField(max_length=500)
    itens = models.ManyToManyField(Item, through='ItemQuestionario')

    def __str__(self):
        return self.descricao


class ItemQuestionario(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_questionario')
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name='item_questionario')


class Alternativa(models.Model):

    descricao = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='alternativa')
    peso = models.IntegerField()

    def __str__(self):
        return self.descricao


class Resposta(models.Model):

    aluno = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='resposta')
    resposta = models.ForeignKey(Alternativa, on_delete=models.CASCADE, related_name='resposta')
    data = models.DateTimeField()




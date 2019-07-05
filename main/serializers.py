import datetime
from typing import Any

from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import TipoPerfil, Curso, Perfil, Area, Item, Questionario, Alternativa, Resposta


class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'})
    email = serializers.EmailField(style={'input_type': 'email'})
    class Meta:
        model = User
        fields = ('url','username','password','first_name', 'last_name', 'email')


class TipoPerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPerfil
        fields = ('url','descricao')


class CursoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Curso
        fields = ('url','descricao', 'nivel', 'tipo','semestre')


class PerfilSerializer(serializers.HyperlinkedModelSerializer):

    # usuario = serializers.ReadOnlyField(source='usuario.username')
    usuario = serializers.HyperlinkedIdentityField(view_name='user-detail', format = 'html')

    class Meta:

        model = Perfil
        fields = ('url','usuario', 'sexo', 'contato', 'tipo_perfil')


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('url','descricao')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url','descricao')


class QuestionarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Questionario
        fields = ('url','autor','area', 'descricao','recomendacoes')


class AlternativaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('url','descricao','item','peso')


class RespostaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resposta
        fields = ('url','aluno', 'resposta')
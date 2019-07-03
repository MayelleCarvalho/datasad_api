from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import TipoPerfil, Curso, Perfil, Area, Item, Questionario, Alternativa, Resposta


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')


class TipoPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPerfil
        fields = ('__all__')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('__all__')


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('__all__')


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('__all__')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


class QuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionario
        fields = ( '__all__')


class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('__all__')


class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ('__all__')
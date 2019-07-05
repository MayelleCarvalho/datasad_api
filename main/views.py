from django.contrib.auth.models import User
from rest_framework import viewsets
from main.models import Curso, TipoPerfil, Perfil, Area, Item, Questionario, Alternativa, Resposta
from main.serializers import UserSerializer, CursoSerializer, PerfilSerializer, AreaSerializer, \
    ItemSerializer, QuestionarioSerializer, AlternativaSerializer, RespostaSerializer, TipoPerfilSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TipoPerfilViewSet(viewsets.ModelViewSet):

    queryset = TipoPerfil.objects.all()
    serializer_class = TipoPerfilSerializer


class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class PerfilViewSet(viewsets.ModelViewSet):

    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class AreaViewSet(viewsets.ModelViewSet):

    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class QuestionarioViewSet(viewsets.ModelViewSet):

    queryset = Questionario.objects.all()
    serializer_class = QuestionarioSerializer


class AlternativaViewSet(viewsets.ModelViewSet):

    queryset = Alternativa.objects.all()
    serializer_class = AreaSerializer


class RespostaViewSet(viewsets.ModelViewSet):

    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
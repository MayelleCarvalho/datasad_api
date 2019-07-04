from django.contrib.auth.models import User
from django.shortcuts import render
from main.permissions import IsOwnerReadOnly

# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from main.models import Curso, TipoPerfil, Perfil, Area, Item, Questionario, Alternativa, Resposta
from main.serializers import UserSerializer, CursoSerializer, PerfilSerializer, AreaSerializer, \
    ItemSerializer, QuestionarioSerializer, AlternativaSerializer, RespostaSerializer, TipoPerfilSerializer


class ApiRoot(generics.GenericAPIView):
	name = 'api-root'
	def get(self,request, *args, **kwargs):
		return Response({
            'usuarios': reverse(UserList.name, request=request),
            'tipo_perfis': reverse(TipoPerfilList.name, request=request),
            'cursos': reverse(CursoList.name, request=request),
            'perfis': reverse(PerfilList.name, request=request),
            'areas': reverse(AreaList.name, request=request),
            'itens': reverse(ItemList.name, request=request),
            'questionarios': reverse(QuestionarioList.name, request=request),
            'alternativas': reverse(AlternativaList.name, request=request),
            'respostas': reverse(RespostaList.name, request=request),
		})


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'


class TipoPerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPerfil.objects.all()
    serializer_class = TipoPerfilSerializer
    name = 'tipo-perfil-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly)


class TipoPerfilList(generics.ListCreateAPIView):
    queryset = TipoPerfil.objects.all()
    serializer_class = TipoPerfilSerializer
    name = 'tipo-perfil-list'


class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    name = 'curso-detail'


class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    name = 'curso-list'


class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    name = 'perfil-detail'


class PerfilList(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    name = 'perfil-list'


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    name = 'area-detail'


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    name = 'area-list'


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    name = 'item-detail'


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    name = 'item-list'


class QuestionarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionario.objects.all()
    serializer_class = QuestionarioSerializer
    name = 'questionario-detail'


class QuestionarioList(generics.ListCreateAPIView):
    queryset = Questionario.objects.all()
    serializer_class = QuestionarioSerializer
    name = 'questionario-list'


class AlternativaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
    name = 'alternativa-detail'


class AlternativaList(generics.ListCreateAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
    name = 'alternativa-list'


class RespostaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    name = 'resposta-detail'


class RespostaList(generics.ListCreateAPIView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    name = 'resposta-list'
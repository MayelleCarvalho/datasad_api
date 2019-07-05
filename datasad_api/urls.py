"""datasad_api URL Configuration

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
from django.urls import path, include
from main import views
from rest_framework.routers import DefaultRouter
from main.views import UserViewSet, CursoViewSet, TipoPerfilViewSet, PerfilViewSet, AreaViewSet, ItemViewSet, \
    QuestionarioViewSet, AlternativaViewSet, RespostaViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

tipoperfil_list = TipoPerfilViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

tipoperfil_detail = TipoPerfilViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

curso_list = CursoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

curso_detail = CursoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

perfil_list = PerfilViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

perfil_detail = PerfilViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

area_list = AreaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

area_detail = AreaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

item_list = ItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

item_detail = ItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

questionario_list = QuestionarioViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

questionario_detail = QuestionarioViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

alternativa_list = AlternativaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

alternativa_detail = AlternativaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

resposta_list = RespostaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

resposta_detail = RespostaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'tipoperfis', views.TipoPerfilViewSet)
router.register(r'cursos', views.CursoViewSet)
router.register(r'perfis', views.PerfilViewSet)
router.register(r'areas', views.AreaViewSet)
router.register(r'itens', views.ItemViewSet)
router.register(r'questionarios', views.QuestionarioViewSet)
router.register(r'alternativas', views.AlternativaViewSet)
router.register(r'respostas', views.RespostaViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

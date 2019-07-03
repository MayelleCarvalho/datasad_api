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
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api/usuarios/<int:pk>', views.UserDetail.as_view(), name = views.UserDetail.name),
    path('api/usuarios/', views.UserList.as_view(), name = views.UserList.name),
    path('api/tipos-perfis/<int:pk>', views.TipoPerfilDetail.as_view(), name=views.TipoPerfilDetail.name),
    path('api/tipos-perfis/', views.TipoPerfilList.as_view(), name=views.TipoPerfilList.name),
    path('api/cursos/<int:pk>', views.CursoDetail.as_view(), name=views.CursoDetail.name),
    path('api/cursos/', views.CursoList.as_view(), name=views.CursoList.name),
    path('api/perfis/<int:pk>', views.PerfilDetail.as_view(), name=views.PerfilDetail.name),
    path('api/perfis/', views.PerfilList.as_view(), name=views.PerfilList.name),
    path('api/areas/<int:pk>', views.AreaDetail.as_view(), name=views.AreaDetail.name),
    path('api/areas/', views.AreaList.as_view(), name=views.AreaList.name),
    path('api/itens/<int:pk>', views.ItemDetail.as_view(), name=views.ItemDetail.name),
    path('api/itens/', views.ItemList.as_view(), name=views.ItemList.name),
    path('api/questionarios/<int:pk>', views.QuestionarioDetail.as_view(), name=views.QuestionarioDetail.name),
    path('api/questionarios/', views.QuestionarioList.as_view(), name=views.QuestionarioList.name),
    path('api/alternativas/<int:pk>', views.AlternativaDetail.as_view(), name=views.AlternativaDetail.name),
    path('api/alternativas/', views.AlternativaList.as_view(), name=views.AlternativaList.name),
    path('api/respostas/<int:pk>', views.RespostaDetail.as_view(), name=views.RespostaDetail.name),
    path('api/respostas/', views.RespostaList.as_view(), name=views.RespostaList.name),
]

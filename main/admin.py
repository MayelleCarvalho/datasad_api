from django.contrib import admin
from main.models import Curso, TipoPerfil, Perfil, Area, Item, Questionario, Alternativa, Resposta


@admin.register(TipoPerfil)
class TipoPerfilAdmin(admin.ModelAdmin):
    pass


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    pass


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    pass
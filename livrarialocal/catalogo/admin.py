from django.contrib import admin

# Register your models here.
from .models import Livro, Autor, Genero, InstanciaDoLivro, Linguagem

@admin.register(Autor)
class AltorAdmin(admin.ModelAdmin):
    list_display = ('primeiro_nome', 'sobre_nome', 'data_de_nascimento', 'data_da_morte')
    fields = ['primeiro_nome', 'sobre_nome', ('data_de_nascimento', 'data_da_morte')]

class LivroInstanceInline(admin.TabularInline):
    model = InstanciaDoLivro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'display_genero', 'foto')
    inlines = [LivroInstanceInline]


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(Linguagem)
class LinguagemAdmin(admin.ModelAdmin):
    pass

@admin.register(InstanciaDoLivro)
class InstanciaDoLivroAdmin(admin.ModelAdmin):
    list_filter = ('status', 'data_retorno')
    fieldsets = (
        (None, {
            'fields': ('livro', 'publicado', 'id')
        }),
        ('Disponibilidade', {
            'fields': ('status', 'data_retorno')
        }),
    )
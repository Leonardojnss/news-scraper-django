from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    """Admin para gerenciar notícias"""
    
    list_display = ['id', 'titulo_resumo', 'fonte', 'data_extracao']
    list_filter = ['fonte', 'data_extracao']
    search_fields = ['titulo', 'descricao']
    readonly_fields = ['data_extracao']
    
    def titulo_resumo(self, obj):
        return obj.titulo[:50] + '...' if len(obj.titulo) > 50 else obj.titulo
    titulo_resumo.short_description = 'Título'


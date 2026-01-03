from django.db import models


class Noticia(models.Model):
    """Model para armazenar notícias extraídas"""
    
    titulo = models.CharField(max_length=500, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição", blank=True)
    link = models.URLField(max_length=1000, verbose_name="Link", blank=True)
    data_extracao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Extração")
    fonte = models.CharField(max_length=200, verbose_name="Fonte", default="G1")
    
    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-data_extracao']
        
    def __str__(self):
        return self.titulo[:50]


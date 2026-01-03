from rest_framework import serializers
from .models import Noticia


class NoticiaSerializer(serializers.ModelSerializer):
    """Serializer para o model Noticia"""
    
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'descricao', 'link', 'data_extracao', 'fonte']
        read_only_fields = ['id', 'data_extracao']

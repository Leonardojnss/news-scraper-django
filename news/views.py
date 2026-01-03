from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Noticia
from .serializers import NoticiaSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar notícias
    
    Endpoints disponíveis:
    - GET /api/noticias/ - Lista todas as notícias
    - POST /api/noticias/ - Cria uma nova notícia
    - GET /api/noticias/{id}/ - Detalhe de uma notícia
    - PUT /api/noticias/{id}/ - Atualiza uma notícia
    - DELETE /api/noticias/{id}/ - Deleta uma notícia
    - DELETE /api/noticias/limpar_tudo/ - Deleta todas as notícias
    """
    
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    
    @action(detail=False, methods=['delete'])
    def limpar_tudo(self, request):
        """Deleta todas as notícias do banco"""
        count = Noticia.objects.count()
        Noticia.objects.all().delete()
        return Response({
            'message': f'{count} notícias deletadas com sucesso'
        }, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def estatisticas(self, request):
        """Retorna estatísticas das notícias"""
        total = Noticia.objects.count()
        fontes = Noticia.objects.values('fonte').distinct().count()
        
        return Response({
            'total_noticias': total,
            'total_fontes': fontes,
        })


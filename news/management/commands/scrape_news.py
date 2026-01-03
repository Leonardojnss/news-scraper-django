"""
Django Management Command para executar o web scraper
"""
from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from news.models import Noticia


class Command(BaseCommand):
    help = 'Executa o web scraper e salva notícias no banco de dados'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            type=str,
            default='https://g1.globo.com/',
            help='URL do site para fazer scraping'
        )
        parser.add_argument(
            '--limpar',
            action='store_true',
            help='Limpa todas as notícias antes de executar o scraper'
        )

    def handle(self, *args, **options):
        url = options['url']
        limpar = options['limpar']
        
        self.stdout.write("\n" + "="*60)
        self.stdout.write(self.style.SUCCESS("🌐 DJANGO WEB SCRAPER DE NOTÍCIAS"))
        self.stdout.write("="*60 + "\n")
        
        # Limpar banco se solicitado
        if limpar:
            count = Noticia.objects.count()
            Noticia.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"🗑️  {count} notícias antigas deletadas\n"))
        
        # Headers para requisição
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            self.stdout.write(f"📡 Buscando: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extrair notícias
            artigos = soup.find_all(['article', 'div'], class_=['noticia', 'post', 'article', 'news-item'])
            
            if not artigos:
                artigos = soup.find_all(['h2', 'h3'])
            
            noticias_salvas = 0
            
            for artigo in artigos[:15]:  # Limita a 15 notícias
                try:
                    # Extrair dados
                    titulo_tag = artigo.find(['h1', 'h2', 'h3', 'h4', 'a'])
                    titulo = titulo_tag.get_text(strip=True) if titulo_tag else ""
                    
                    if len(titulo) < 10:
                        continue
                    
                    link_tag = artigo.find('a', href=True)
                    link = link_tag['href'] if link_tag else ""
                    
                    if link and not link.startswith('http'):
                        link = url.rstrip('/') + '/' + link.lstrip('/')
                    
                    descricao_tag = artigo.find(['p', 'span', 'div'], class_=['resumo', 'description', 'excerpt'])
                    descricao = descricao_tag.get_text(strip=True) if descricao_tag else ""
                    
                    # Salvar no banco
                    Noticia.objects.create(
                        titulo=titulo[:500],
                        descricao=descricao[:1000] if descricao else "Sem descrição",
                        link=link[:1000] if link else "",
                        fonte="G1"
                    )
                    
                    noticias_salvas += 1
                    self.stdout.write(self.style.SUCCESS(f"✓ {titulo[:60]}..."))
                    
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"✗ Erro ao processar artigo: {e}"))
                    continue
            
            self.stdout.write("\n" + "="*60)
            self.stdout.write(self.style.SUCCESS(f"✅ {noticias_salvas} notícias salvas no banco de dados!"))
            self.stdout.write(self.style.SUCCESS(f"📊 Total no banco: {Noticia.objects.count()} notícias"))
            self.stdout.write("="*60 + "\n")
            
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"\n❌ Erro ao fazer scraping: {e}\n"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"\n❌ Erro inesperado: {e}\n"))

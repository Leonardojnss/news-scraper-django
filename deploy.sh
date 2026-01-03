# 🚀 Deploy Script para AWS EC2
# Execute este script no servidor EC2 após clonar o repositório

#!/bin/bash

set -e

echo "🚀 Iniciando deploy do News Scraper..."

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar se está rodando como root
if [ "$EUID" -eq 0 ]; then 
    echo "❌ Não execute como root. Use: bash deploy.sh"
    exit 1
fi

# Verificar se arquivo .env existe
if [ ! -f .env ]; then
    echo "❌ Arquivo .env não encontrado!"
    echo "📝 Copie .env.example para .env e configure:"
    echo "   cp .env.example .env"
    echo "   nano .env"
    exit 1
fi

echo "${GREEN}✓${NC} Arquivo .env encontrado"

# Ativar ambiente virtual
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

source venv/bin/activate
echo "${GREEN}✓${NC} Ambiente virtual ativado"

# Instalar dependências
echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt
echo "${GREEN}✓${NC} Dependências instaladas"

# Executar migrações
echo "🗄️  Executando migrações..."
python manage.py migrate --noinput
echo "${GREEN}✓${NC} Migrações concluídas"

# Coletar arquivos estáticos
echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput
echo "${GREEN}✓${NC} Arquivos estáticos coletados"

# Verificar se superusuário existe
echo "👤 Verificando superusuário..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    print('${YELLOW}⚠️  Superusuário não existe. Crie um:${NC}')
    print('   python manage.py createsuperuser')
else:
    print('${GREEN}✓${NC} Superusuário já existe')
END

# Testar configurações Django
echo "🔍 Testando configurações Django..."
python manage.py check --deploy
echo "${GREEN}✓${NC} Configurações OK"

# Reiniciar serviço Gunicorn (se existir)
if systemctl is-active --quiet news-scraper; then
    echo "🔄 Reiniciando serviço Gunicorn..."
    sudo systemctl restart news-scraper
    echo "${GREEN}✓${NC} Serviço reiniciado"
else
    echo "${YELLOW}⚠️  Serviço news-scraper não encontrado${NC}"
    echo "   Configure o systemd service primeiro"
fi

# Reiniciar Nginx (se instalado)
if command -v nginx &> /dev/null; then
    echo "🔄 Reiniciando Nginx..."
    sudo systemctl reload nginx
    echo "${GREEN}✓${NC} Nginx recarregado"
fi

echo ""
echo "${GREEN}✅ Deploy concluído com sucesso!${NC}"
echo ""
echo "🌐 Acesse sua aplicação:"
echo "   Frontend: http://seu-dominio.com/frontend/index.html"
echo "   Admin: http://seu-dominio.com/admin/"
echo "   API: http://seu-dominio.com/api/noticias/"
echo ""
echo "📊 Comandos úteis:"
echo "   Ver logs: sudo journalctl -u news-scraper -f"
echo "   Status: sudo systemctl status news-scraper"
echo "   Scraping: source venv/bin/activate && python manage.py scrape_news"

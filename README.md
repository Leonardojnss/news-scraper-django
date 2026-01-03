# 📰 News Scraper - Django REST Framework + Frontend

Projeto profissional de Web Scraping com **Django**, **Django REST Framework** e **Frontend JavaScript**. Sistema completo de extração, armazenamento e visualização de notícias.

## ⚡ Início Rápido

### 🐳 Com Docker (Recomendado)

```bash
# 1. Iniciar com Docker Compose
docker-compose up -d

# 2. Acessar aplicação
Frontend: http://localhost:8000/frontend/index.html
API: http://localhost:8000/api/noticias/
Admin: http://localhost:8000/admin/ (admin/admin123)

# 3. Fazer scraping de notícias
docker-compose exec web python manage.py scrape_news

# 4. Ver logs
docker-compose logs -f web

# 5. Parar containers
docker-compose down
```

### 💻 Instalação Manual

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar banco de dados
python manage.py migrate

# 3. Criar superusuário (acesso ao admin)
python manage.py createsuperuser

# 4. Fazer scraping de notícias
python manage.py scrape_news

# 5. Iniciar servidor
python manage.py runserver

# 6. Acessar aplicação
Frontend: http://localhost:8000/frontend/index.html
API: http://localhost:8000/api/noticias/
Admin: http://localhost:8000/admin/
```

## 🎯 Objetivo

Sistema completo de web scraping que:
- Extrai notícias de sites brasileiros automaticamente
- Armazena dados em banco de dados Django (PostgreSQL ou SQLite)
- Disponibiliza API REST completa (DRF)
- Interface frontend moderna consumindo a API
- Painel administrativo Django customizado

## ✨ Funcionalidades

### Backend (Django + DRF)
- ✅ **API REST completa** - CRUD de notícias
- ✅ **Django REST Framework** - Serializers e ViewSets
- ✅ **PostgreSQL/SQLite** - Banco de dados configurável
- ✅ **Docker + Docker Compose** - Containerização completa
- ✅ **Admin Django customizado** - Gerenciamento visual
- ✅ **Management Commands** - Automação de scraping
- ✅ **Paginação automática** - Listagem otimizada
- ✅ **CORS configurado** - Pronto para produção
- ✅ **Endpoints de estatísticas** - Análise de dados
- ✅ **Variáveis de ambiente** - Configuração segura

### Frontend (HTML/CSS/JavaScript)
- ✅ **Interface moderna e responsiva**
- ✅ **Consumo de API REST** com Fetch API
- ✅ **Grid de notícias** com animações CSS
- ✅ **Botões de ação** (recarregar, limpar, estatísticas)
## 📦 Dependências

### Backend
- **Python 3.13+**
- **Django 5.0** - Framework web full-featured
- **Django REST Framework 3.14** - API RESTful
- **django-cors-headers** - Configuração CORS
- **PostgreSQL** - Banco de dados (produção) - opcional
- **SQLite** - Banco de dados (desenvolvimento) - padrão
- **psycopg2-binary** - Driver PostgreSQL
- **python-dotenv** - Variáveis de ambiente
- **BeautifulSoup4 4.12** - Parse de HTML
- **Requests 2.31** - Requisições HTTP

### Infraestrutura
- **Docker** - Containerização
- **Docker Compose** - Orquestração de containers
- **PostgreSQL 16** (Alpine) - Banco de dados em container

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Grid, Flexbox, animações e gradientes
- **JavaScript (ES6+)** - Async/await, Fetch API
- **Vanilla JS** - Sem dependências de framework

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.13+**
- **BeautifulSoup4** - Parse de HTML
- **Requests** - Requisições HTTP
- **CSV & JSON** - Manipulação de dados

### Frontend
- **HTML5** - Estrutura da página
- **CSS3** - Estilização e animações
- **JavaScript (Vanilla)** - Interatividade e carregamento de dados

- Navegador web moderno

## 🚀 Instalação Detalhada
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🚀 Como Usar

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd "News Scraper"
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
```

### 3. Ative o ambiente virtual
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Configure o banco de dados

**Opção A: SQLite (padrão, mais fácil)**
```bash
# Nenhuma configuração adicional necessária
# O arquivo db.sqlite3 será criado automaticamente
```

**Opção B: PostgreSQL (produção)**
```bash
# 1. Instale PostgreSQL no seu sistema
# 2. Crie um banco de dados
# 3. Copie o arquivo de exemplo
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac

# 4. Edite o arquivo .env com suas credenciais:
# DB_NAME=news_scraper_db
# DB_USER=seu_usuario
# DB_PASSWORD=sua_senha
# DB_HOST=localhost
# DB_PORT=5432
# USE_SQLITE=False
```

### 6. Execute as migrações
### 6. Execute as migrações
```bash
python manage.py migrate
```

### 7. Crie um superusuário (para acessar o admin)
```bash
python manage.py createsuperuser
# Siga as instruções: username, email, password
```

**Credenciais de teste configuradas:**
- **Usuário**: `teste`
- **Senha**: `teste123`

### 8. Execute o scraping inicial
```bash
python manage.py scrape_news
```

### 9. Inicie o servidor Django
```bash
python manage.py runserver
```

### 10. Acesse a aplicação
- **Frontend**: http://localhost:8000/frontend/index.html
- **API REST**: http://localhost:8000/api/noticias/
- **Admin Django**: http://localhost:8000/admin/ (user: `teste` | senha: `teste123`)

## 🐘 Configuração PostgreSQL (Opcional)

### Windows
```bash
# 1. Baixe e instale PostgreSQL: https://www.postgresql.org/download/windows/

# 2. Abra pgAdmin ou use psql para criar banco:
createdb news_scraper_db

# 3. Configure variáveis de ambiente no .env
```

### Linux (Ubuntu/Debian)
```bash
# 1. Instale PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# 2. Crie usuário e banco
sudo -u postgres psql
CREATE DATABASE news_scraper_db;
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
ALTER ROLE seu_usuario SET client_encoding TO 'utf8';
ALTER ROLE seu_usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE seu_usuario SET timezone TO 'America/Sao_Paulo';
GRANT ALL PRIVILEGES ON DATABASE news_scraper_db TO seu_usuario;
\q

# 3. Configure o arquivo .env
```

### macOS
```bash
# 1. Instale PostgreSQL via Homebrew
brew install postgresql
brew services start postgresql

# 2. Crie banco de dados
createdb news_scraper_db

# 3. Configure o arquivo .env
```

## 🔒 Variáveis de Ambiente

O projeto usa um arquivo `.env` para configurações sensíveis. Copie o `.env.example`:

```bash
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac
```

Edite o `.env` conforme necessário:

```env
# Database (PostgreSQL)
DB_NAME=news_scraper_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Use SQLite ao invés de PostgreSQL
USE_SQLITE=False  # True para desenvolvimento com SQLite

# Django
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
```

**⚠️ IMPORTANTE**: Nunca commite o arquivo `.env` no Git! Ele já está no `.gitignore`.

## 📂 Estrutura do Projeto

```
News Scraper/
├── config/                 # Configurações Django
│   ├── settings.py        # Configurações (PostgreSQL/SQLite)
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # WSGI config
│
├── news/                   # App Django principal
│   ├── models.py          # Model Noticia
│   ├── serializers.py     # Serializers DRF
│   ├── views.py           # ViewSets API
│   ├── urls.py            # URLs da API
│   ├── admin.py           # Admin customizado
│   ├── migrations/        # Migrações do banco
│   └── management/        # Comandos customizados
│       └── commands/
│           └── scrape_news.py
│
├── frontend/              # Frontend JavaScript
│   ├── index.html        # Interface principal
│   ├── styles.css        # Estilos CSS
│   └── app.js            # Lógica JavaScript
│
├── .env.example          # Template de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── requirements.txt       # Dependências Python
├── manage.py             # CLI Django
└── README.md             # Documentação
```

## ⚙️ Comandos Django Úteis

### Scraping de Notícias
```bash
# Fazer scraping padrão (G1)
python manage.py scrape_news

# Limpar banco e fazer scraping
python manage.py scrape_news --limpar

# Scraping de URL customizada
python manage.py scrape_news --url https://outro-site.com
```

### Gerenciamento do Banco
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Shell interativo Django
python manage.py shell

# Criar superusuário
python manage.py createsuperuser
```

## 📡 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/noticias/` | Lista todas notícias (paginado) |
| POST | `/api/noticias/` | Cria nova notícia |
| GET | `/api/noticias/{id}/` | Detalhes de uma notícia |
| PUT | `/api/noticias/{id}/` | Atualiza notícia |
| DELETE | `/api/noticias/{id}/` | Deleta notícia |
| DELETE | `/api/noticias/limpar_tudo/` | Deleta todas notícias |
| GET | `/api/noticias/estatisticas/` | Estatísticas do banco |

### Exemplo de Requisição
```bash
# Listar notícias
curl http://localhost:8000/api/noticias/

# Obter estatísticas
curl http://localhost:8000/api/noticias/estatisticas/
```

### Exemplo de Resposta JSON
```json
{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "titulo": "Título da Notícia",
            "descricao": "Descrição...",
            "link": "https://g1.globo.com/...",
            "data_extracao": "2026-01-02T23:10:00Z",
            "fonte": "G1"
        }
    ]
}. Clique com botão direito > Inspecionar
3. Identifique as tags HTML e classes das notícias
4. Atualize os seletores no código

## 📊 Formato dos Dados

### CSV
```csv
id,titulo,descricao,link,data_extracao
1,"Título da Notícia","Descrição breve...","https://...","2026-01-02 10:30:00"
```

### JSON
```json
[
    {
        "id": 1,
        "titulo": "Título da Notícia",
        "descricao": "Descrição breve...",
        "link": "https://...",
        "data_extracao": "2026-01-02 10:30:00"
    }
]
```

## 🐳 Docker

### Por que Docker?

- **Portabilidade**: Funciona em qualquer máquina com Docker
- **Consistência**: Mesmo ambiente em desenvolvimento e produção
- **Isolamento**: Não interfere com outras instalações
- **Facilidade**: Um comando para subir tudo

### Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado
- Docker Compose (incluído no Docker Desktop)

### Comandos Docker

```bash
# Iniciar containers (primeira vez ou após mudanças)
docker-compose up --build

# Iniciar em background
docker-compose up -d

# Ver logs em tempo real
docker-compose logs -f
docker-compose logs -f web    # Apenas da aplicação
docker-compose logs -f db     # Apenas do PostgreSQL

# Executar comandos dentro do container
docker-compose exec web python manage.py scrape_news
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py shell

# Acessar terminal do container
docker-compose exec web bash
docker-compose exec db psql -U postgres -d news_scraper_db

# Parar containers (mantém dados)
docker-compose stop

# Parar e remover containers
docker-compose down

# Parar, remover E deletar volumes (CUIDADO: perde dados!)
docker-compose down -v

# Rebuild após mudanças no código
docker-compose up --build

# Ver status dos containers
docker-compose ps

# Ver uso de recursos
docker stats
```

### Estrutura Docker

```
News Scraper/
├── Dockerfile              # Imagem da aplicação Django
├── docker-compose.yml      # Orquestração (Django + PostgreSQL)
├── .dockerignore          # Arquivos ignorados no build
└── entrypoint.sh          # Script de inicialização
```

### Volumes Docker

Os dados do PostgreSQL são persistidos em um volume Docker:
- **postgres_data**: Banco de dados (não é perdido ao parar containers)

### Variáveis de Ambiente Docker

Configuradas no `docker-compose.yml`:
- `DEBUG=True` - Modo debug (mudar para False em produção)
- `DB_HOST=db` - Nome do serviço PostgreSQL no Docker
- `DB_NAME=news_scraper_db` - Nome do banco
- `DB_USER=postgres` - Usuário PostgreSQL
- `DB_PASSWORD=postgres` - Senha PostgreSQL

### Troubleshooting Docker

**Erro de porta já em uso:**
```bash
# Altere a porta no docker-compose.yml
ports:
  - "8001:8000"  # Usar porta 8001 ao invés de 8000
```

**Container não inicia:**
```bash
# Ver logs detalhados
docker-compose logs web

# Rebuild forçado
docker-compose build --no-cache
docker-compose up
```

**Resetar tudo:**
```bash
# CUIDADO: Apaga TUDO (dados, volumes, containers)
docker-compose down -v
docker-compose up --build
```

## ⚠️ Considerações Legais e Éticas
utenticação JWT para API
- [ ] Testes automatizados (pytest, unittest)
- [ ] Deploy em produção (Heroku, Railway, AWS)
- [ ] PostgreSQL em produção
- [ ] Docker e docker-compose
- [ ] Celery para scraping assíncrono
- [ ] Agendamento de scraping (Celery Beat)
- [ ] Frontend em React ou Vue.js
- [ ] WebSockets para atualizações em tempo real
- [ ] Análise de sentimentos com NLP
- [ ] Cache com Redis
- [ ] Integração com múltiplas fontes de notíciacacionais

## 🎓 Habilidades DemonstradasFull-Stack demonstrando:
- Backend Django + Django REST Framework
- Frontend JavaScript puro (Vanilla JS)
- Web Scraping profissional
- Integração completa de sistemas

Ideal para vagas de **Desenvolvedor Python Júnior/Pleno** e **Desenvolvedor Full-Stack**.

---

⭐ **Nota para Recrutadores**: 
- Sistema completo e funcional
- Código limpo e documentado
- Arquitetura profissional
- Boas práticas da indústria
- Pronto para produção (com ajustes)

📧 Contato para oportunidades de trabalho!
### Backend
- Programação Orientada a Objetos (OOP)
- Manipulação de requisições HTTP
- Parse e análise de HTML
- Tratamento de exceções
- Manipulação de arquivos
- Boas práticas de Python (PEP 8)

### Frontend
- HTML5 semântico
- CSS3 com Flexbox e Grid
- JavaScript assíncrono (async/await)
- Fetch API
- Manipulação do DOM
- Design responsivo
- Animações CSS

### Geral
- Documentação de código
- Integração Frontend-Backend
- Desenvolvimento Full-Stack básico
- Boas práticas de Python (PEP 8)

## � Deploy na AWS EC2

### Pré-requisitos

- Conta AWS ativa
- EC2 instance (Ubuntu 22.04 LTS recomendado)
- Par de chaves SSH (.pem)
- Security Group com portas abertas: 22 (SSH), 80 (HTTP), 443 (HTTPS), 8000 (Django)

### Passo a Passo

#### 1. Conectar ao EC2

```bash
# Alterar permissões da chave
chmod 400 sua-chave.pem

# Conectar via SSH
ssh -i sua-chave.pem ubuntu@seu-ec2-ip
```

#### 2. Instalar Dependências no Servidor

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python e dependências
sudo apt install -y python3-pip python3-venv postgresql postgresql-contrib nginx git

# Instalar Docker (opcional, para usar containers)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
```

#### 3. Clonar Projeto

```bash
# Criar diretório
mkdir -p ~/apps
cd ~/apps

# Clonar repositório
git clone https://github.com/seu-usuario/news-scraper.git
cd news-scraper
```

#### 4. Configurar PostgreSQL

```bash
# Acessar PostgreSQL
sudo -u postgres psql

# Dentro do psql:
CREATE DATABASE news_scraper_db;
CREATE USER news_user WITH PASSWORD 'senha_segura_aqui';
ALTER ROLE news_user SET client_encoding TO 'utf8';
ALTER ROLE news_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE news_user SET timezone TO 'America/Sao_Paulo';
GRANT ALL PRIVILEGES ON DATABASE news_scraper_db TO news_user;
\q
```

#### 5. Configurar Ambiente Python

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt
```

#### 6. Configurar Variáveis de Ambiente

```bash
# Criar arquivo .env
nano .env

# Adicionar (pressione Ctrl+X, Y, Enter para salvar):
DEBUG=False
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com,seu-ec2-ip,localhost,127.0.0.1
FORCE_SCRIPT_NAME=/news-scraper
DB_NAME=news_scraper_db
DB_USER=news_user
DB_PASSWORD=senha_segura_aqui
DB_HOST=localhost
DB_PORT=5432
USE_SQLITE=False
```

**⚠️ IMPORTANTE**: Ajustar permissões do diretório home para o Nginx acessar arquivos estáticos:

```bash
chmod 755 /home/ubuntu
chmod 755 /home/ubuntu/apps
chmod 755 /home/ubuntu/apps/news-scraper
chmod -R 755 ~/apps/news-scraper/staticfiles/
```

#### 7. Preparar Django

```bash
# Executar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Testar servidor
python manage.py runserver 0.0.0.0:8000
# Acesse http://seu-ec2-ip:8000
# Pressione Ctrl+C para parar
```

#### 8. Configurar Gunicorn como Serviço

```bash
# Criar arquivo de serviço systemd
sudo nano /etc/systemd/system/news-scraper.service
```

Adicione:

```ini
[Unit]
Description=News Scraper Gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/apps/news-scraper
Environment="PATH=/home/ubuntu/apps/news-scraper/venv/bin"
EnvironmentFile=/home/ubuntu/apps/news-scraper/.env
ExecStart=/home/ubuntu/apps/news-scraper/venv/bin/gunicorn \
          --config gunicorn_config.py \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Habilitar e iniciar serviço
sudo systemctl daemon-reload
sudo systemctl start news-scraper
sudo systemctl enable news-scraper
sudo systemctl status news-scraper
```

#### 9. Configurar Nginx

```bash
# Criar configuração do site
sudo nano /etc/nginx/sites-available/news-scraper
```

Adicione:

```nginx
server {
    listen 80 default_server;
    server_name seu-dominio.com www.seu-dominio.com seu-ec2-ip;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /news-scraper/static/ {
        alias /home/ubuntu/apps/news-scraper/staticfiles/;
    }

    location /news-scraper/ {
        proxy_pass http://127.0.0.1:8001/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# Ativar site
sudo ln -s /etc/nginx/sites-available/news-scraper /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 10. Configurar HTTPS com Let's Encrypt (Opcional mas Recomendado)

```bash
# Instalar Certbot
sudo apt install -y certbot python3-certbot-nginx

# Obter certificado SSL
sudo certbot --nginx -d seu-dominio.com -d www.seu-dominio.com

# Renovação automática (já configurado pelo Certbot)
sudo systemctl status certbot.timer
```

### Deploy com Docker (Alternativa)

```bash
# No servidor EC2
cd ~/apps/news-scraper

# Build e start
docker-compose -f docker-compose.prod.yml up -d --build

# Ver logs
docker-compose logs -f web
```

### Comandos Úteis no Servidor

```bash
# Ver logs do Gunicorn
sudo journalctl -u news-scraper -f

# Reiniciar serviço
sudo systemctl restart news-scraper

# Ver logs do Nginx
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Atualizar código
cd ~/apps/news-scraper
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart news-scraper
```

### Segurança Adicional

```bash
# Configurar firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

# Desabilitar acesso direto à porta 8000
# (Nginx faz proxy reverso)
```

### Backup do Banco de Dados

```bash
# Exportar banco
pg_dump -U news_user news_scraper_db > backup_$(date +%Y%m%d).sql

# Restaurar banco
psql -U news_user news_scraper_db < backup_20260103.sql
```

### Monitoramento

```bash
# Instalar htop para monitorar recursos
sudo apt install -y htop
htop

# Ver processos do Gunicorn
ps aux | grep gunicorn

# Ver uso de memória
free -h

# Ver uso de disco
df -h
```

### Troubleshooting

**Erro 502 Bad Gateway:**
```bash
# Verificar status do Gunicorn
sudo systemctl status news-scraper

# Ver logs
sudo journalctl -u news-scraper -n 50
```

**Static files não carregam:**
```bash
# Coletar novamente
source venv/bin/activate
python manage.py collectstatic --noinput
sudo systemctl restart nginx
```

**Erro de conexão com banco:**
```bash
# Verificar PostgreSQL
sudo systemctl status postgresql

# Testar conexão
psql -U news_user -d news_scraper_db -h localhost
```

## �🔄 Melhorias Futuras

- [ ] Adicionar suporte a múltiplas páginas (paginação)
- [ ] Implementar banco de dados (SQLite/PostgreSQL)
- [ ] Criar interface gráfica (GUI)
- [ ] Adicionar agendamento automático
- [ ] Implementar análise de sentimentos
- [ ] Dashboard de visualização de dados

## 📝 Licença

Projeto de uso livre para fins educacionais e de portfolio.

## 👤 Autor

Desenvolvido como projeto portfolio para vaga de desenvolvedor júnior.

---

⭐ Se este projeto foi útil, considere dar uma estrela no repositório!

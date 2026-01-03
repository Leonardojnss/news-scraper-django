# 📰 News Scraper - Django REST Framework + Frontend

Projeto profissional de Web Scraping com **Django**, **Django REST Framework** e **Frontend JavaScript**. Sistema completo de extração, armazenamento e visualização de notícias.

## ⚡ Início Rápido

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
- Armazena dados em banco de dados Django (SQLite)
- Disponibiliza API REST completa (DRF)
- Interface frontend moderna consumindo a API
- Painel administrativo Django customizado

## ✨ Funcionalidades

### Backend (Django + DRF)
- ✅ **API REST completa** - CRUD de notícias
- ✅ **Django REST Framework** - Serializers e ViewSets
- ✅ **Admin Django customizado** - Gerenciamento visual
- ✅ **Management Commands** - Automação de scraping
- ✅ **Paginação automática** - Listagem otimizada
- ✅ **CORS configurado** - Pronto para produção
- ✅ **Endpoints de estatísticas** - Análise de dados

### Frontend (HTML/CSS/JavaScript)
- ✅ **Interface moderna e responsiva**
- ✅ **Consumo de API REST** com Fetch API
- ✅ **Grid de notícias** com animações CSS
- ✅ **Botões de ação** (recarregar, limpar, estatísticas)
- ✅ Django 5.0** - Framework web full-featured
- **Django REST Framework 3.14** - API RESTful
- **django-cors-headers** - Configuração CORS
- **SQLite** - Banco de dados (desenvolvimento)
- **BeautifulSoup4 4.12** - Parse de HTML
- **Requests 2.31** - Requisições HTTP

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
Configure o banco de dados
```bash
python manage.py migrate
```

### 6. Crie um superusuário (para acessar o admin)
```bash
python manage.py createsuperuser
# Siga as instruções: username, email, password
```

**Credenciais de teste configuradas:**
- **Usuário**: `teste`
- **Senha**: `teste123`

### 7. Execute o scraping inicial
```bash
python manage.py scrape_news
```

### 8. Inicie o servidor Django
```bash
python manage.py runserver
```

### 9. Acesse a aplicação
- **Frontend**: http://localhost:8000/frontend/index.html
- **API REST**: http://localhost:8000/api/noticias/
- **Admin Django**: http://localhost:8000/admin/ (user: `teste` | senha: `teste123`)p://localhost:8000
```

## config/                  # Configurações Django
│   ├── settings.py         # Configurações do projeto
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
│   └─Comandos Django Úteis

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

## 🔄 Melhorias Futuras

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

# Usar Python 3.13 como base
FROM python:3.13-slim

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Criar diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para PostgreSQL e compilação
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar diretório para arquivos estáticos
RUN mkdir -p staticfiles

# Expor porta 8000
EXPOSE 8000

# Tornar o entrypoint executável
RUN chmod +x /app/entrypoint.sh

# Definir entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Comando padrão para produção (Gunicorn)
CMD ["gunicorn", "--config", "gunicorn_config.py", "config.wsgi:application"]

#!/bin/bash

# Sair em caso de erro
set -e

echo "🐘 Aguardando PostgreSQL ficar disponível..."
while ! pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER > /dev/null 2>&1; do
    sleep 1
done
echo "✅ PostgreSQL está pronto!"

echo "🔄 Executando migrações..."
python manage.py migrate --noinput

echo "📊 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear || true

echo "👤 Criando superusuário (se não existir)..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
    print('✅ Superusuário criado: admin/admin123')
else:
    print('ℹ️  Superusuário já existe')
END

echo "🚀 Iniciando servidor Django..."
exec "$@"

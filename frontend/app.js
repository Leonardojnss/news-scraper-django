// Configuração da API
const API_URL = '/news-scraper/api/noticias/';

// Função para carregar notícias da API
async function carregarNoticias() {
    const container = document.getElementById('newsContainer');
    const totalElement = document.getElementById('totalNoticias');
    
    container.innerHTML = '<div class="loading">Carregando notícias da API Django...</div>';
    totalElement.textContent = '';

    try {
        const response = await fetch(API_URL);
        
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }

        const data = await response.json();
        const noticias = data.results || data; // Suporta paginação do DRF
        
        if (noticias.length === 0) {
            container.innerHTML = `
                <div class="empty">
                    <h2>📭 Nenhuma notícia encontrada</h2>
                    <p>Execute o comando Django para fazer scraping:</p>
                    <code>python manage.py scrape_news</code>
                </div>
            `;
            return;
        }

        // Exibir total
        totalElement.textContent = `Total: ${noticias.length} notícia${noticias.length > 1 ? 's' : ''}`;

        // Criar grid de notícias
        container.innerHTML = '<div class="news-grid"></div>';
        const grid = container.querySelector('.news-grid');

        noticias.forEach(noticia => {
            const card = criarCardNoticia(noticia);
            grid.appendChild(card);
        });

        console.log('✅ Notícias carregadas da API:', noticias.length);

    } catch (error) {
        console.error('Erro:', error);
        container.innerHTML = `
            <div class="error">
                <h2>❌ Erro ao carregar notícias da API</h2>
                <p>${error.message}</p>
                <p>Certifique-se de que o servidor Django está rodando:</p>
                <code>python manage.py runserver</code>
                <p style="margin-top: 10px;">E que a API está acessível em: <strong>${API_URL}</strong></p>
            </div>
        `;
    }
}

// Função para criar card de notícia
function criarCardNoticia(noticia) {
    const card = document.createElement('div');
    card.className = 'news-card';
    
    const titulo = noticia.titulo || 'Sem título';
    const descricao = noticia.descricao || 'Sem descrição';
    const link = noticia.link || '#';
    const dataExtracao = noticia.data_extracao || '';
    const id = noticia.id || '0';
    const fonte = noticia.fonte || 'Desconhecida';

    card.innerHTML = `
        <div class="meta">
            <span class="badge">#${id}</span>
            <span class="fonte-badge">${escapeHtml(fonte)}</span>
            <span>📅 ${formatarData(dataExtracao)}</span>
        </div>
        <h3>${escapeHtml(titulo)}</h3>
        <p>${escapeHtml(descricao)}</p>
        ${link !== '#' ? `<a href="${link}" target="_blank" class="link">Ler notícia completa →</a>` : ''}
    `;

    return card;
}

// Função para formatar data
function formatarData(dataString) {
    if (!dataString) return 'Data desconhecida';
    
    try {
        const data = new Date(dataString);
        return data.toLocaleDateString('pt-BR', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    } catch {
        return dataString;
    }
}

// Função para escapar HTML (segurança)
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Função para limpar todas as notícias do banco
async function limparTodasNoticias() {
    if (!confirm('⚠️ Tem certeza que deseja deletar TODAS as notícias do banco de dados?')) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}limpar_tudo/`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error('Erro ao limpar notícias');
        }

        const data = await response.json();
        alert(`✅ ${data.message}`);
        
        // Recarregar notícias
        carregarNoticias();

    } catch (error) {
        alert(`❌ Erro: ${error.message}`);
        console.error('Erro ao limpar:', error);
    }
}

// Função para ver estatísticas
async function verEstatisticas() {
    const statsContainer = document.getElementById('statsContainer');
    
    try {
        const response = await fetch(`${API_URL}estatisticas/`);
        
        if (!response.ok) {
            throw new Error('Erro ao carregar estatísticas');
        }

        const stats = await response.json();
        
        statsContainer.style.display = 'block';
        statsContainer.innerHTML = `
            <h2 style="margin-bottom: 20px; color: #2c3e50;">📊 Estatísticas do Banco de Dados</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>${stats.total_noticias}</h3>
                    <p>Total de Notícias</p>
                </div>
                <div class="stat-card">
                    <h3>${stats.total_fontes}</h3>
                    <p>Fontes Diferentes</p>
                </div>
            </div>
        `;

        // Auto-esconder após 5 segundos
        setTimeout(() => {
            statsContainer.style.display = 'none';
        }, 5000);

    } catch (error) {
        alert(`❌ Erro: ${error.message}`);
        console.error('Erro nas estatísticas:', error);
    }
}

// Carregar notícias ao abrir a página
window.addEventListener('DOMContentLoaded', carregarNoticias);

// Recarregar automaticamente a cada 30 segundos (opcional)
// setInterval(carregarNoticias, 30000);

# 🎮 LoL Counter-Pick Scraper & Automation Bot

> Bot de Discord que busca, em tempo real, os counters de qualquer campeão de League of Legends para ajudar na fase de Draft.

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![Discord](https://img.shields.io/badge/discord.py-API-5865F2?style=for-the-badge&logo=discord)
![BeautifulSoup](https://img.shields.io/badge/Web_Scraping-BS4-43B02A?style=for-the-badge)

## 📌 Sobre o projeto

Este projeto nasceu da necessidade de agilizar a tomada de decisão durante o **Draft** (seleção de personagens) no League of Legends.

O bot funciona como um pequeno pipeline de dados: recebe o nome do campeão no Discord, faz **web scraping** em tempo real no site [League of Graphs](https://www.leagueofgraphs.com/pt), limpa o HTML bruto e devolve só o que importa, os **counters**, em uma mensagem organizada.

## 💬 Como usar

No servidor do Discord onde o bot estiver, digite:

```
!counters Renata Glasc
```

O bot responde com os 5 campeões que têm melhor desempenho contra o escolhido, em um *embed* colorido.

## ⚙️ Funcionalidades técnicas

- **Extração de dados:** requisição HTTP com `requests` para baixar a página do campeão.
- **Limpeza de dados:** normalização de nomes (acentos, espaços, apóstrofos) e exceções conhecidas, como "Renata Glasc" → `renata` e "Wukong" → `monkeyking`.
- **Parsing:** `BeautifulSoup4` para navegar no HTML e isolar a tabela de estatísticas, com um plano B se a página mudar de formato.
- **Segurança:** o token do bot fica em variável de ambiente (`.env`) e nunca vai para o repositório.

## 🛠️ Tecnologias

- Python 3.12+
- `discord.py`: interface do bot
- `beautifulsoup4`: leitura do HTML
- `requests`: requisições HTTP
- `python-dotenv`: variáveis de ambiente

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/julianpbarbosa/lol-counter-picker-scraper.git
cd lol-counter-picker-scraper
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Crie o bot no Discord

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications) e crie uma aplicação.
2. Em **Bot**, copie o **token**.
3. Ainda em **Bot**, ative **Message Content Intent** (sem isso o bot não lê os comandos).
4. Em **OAuth2 > URL Generator**, marque `bot` e a permissão de enviar mensagens, e use o link gerado para adicionar o bot ao seu servidor.

### 4. Configure o token

Copie o arquivo de exemplo e coloque o seu token:

```bash
cp .env.example .env
```

No Windows (PowerShell): `Copy-Item .env.example .env`

Abra o `.env` e troque `SEU_TOKEN_AQUI_SEM_ASPAS` pelo token do seu bot, sem aspas.

### 5. Rode

```bash
python main.py
```

Quando aparecer `🤖 Bot conectado como ...`, o bot está pronto.

## ⚠️ Limitações e avisos

- Os dados vêm do HTML do League of Graphs. **Se o site mudar o layout, a extração pode parar de funcionar** e o bot avisa no chat.
- Use com moderação e respeite os termos de uso do site de origem. O projeto é para estudo.
- Projeto não oficial. Não é afiliado nem endossado pela Riot Games. *League of Legends* é marca da Riot Games, Inc.

## 📚 O que este projeto me ensinou

Consumo de HTML com `requests` e `BeautifulSoup`, tratamento e normalização de texto, bots assíncronos com `discord.py` e boas práticas com credenciais (`.env` e `.gitignore`).

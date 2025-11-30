# 🎮 LoL Counter-Pick Scraper & Automation Bot

> Ferramenta de automação e extração de dados (Web Scraping) integrada ao Discord para análise de estratégia em tempo real.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Discord](https://img.shields.io/badge/Discord.py-API-5865F2?style=for-the-badge&logo=discord)
![BeautifulSoup](https://img.shields.io/badge/Web_Scraping-BS4-43B02A?style=for-the-badge)

## 📌 Sobre o Projeto
Este projeto nasceu da necessidade de agilizar a tomada de decisão durante a fase de "Draft" (seleção de personagens) no League of Legends. 

Desenvolvi um bot que atua como um pipeline de dados simplificado: ele recebe um input do usuário, realiza um **Web Scraping** em tempo real no site *League of Graphs*, processa o HTML bruto para limpar os dados e retorna apenas as informações estratégicas (os "Counters") de forma estruturada.

## ⚙️ Funcionalidades Técnicas
* **Extração de Dados (ETL):** Conexão via `requests` para baixar o HTML da página do campeão.
* **Limpeza de Dados:** Tratamento de strings e normalização de nomes (ex: conversão de "Renata Glasc" para slug de URL `renata`, tratamento de acentos).
* **Parsing:** Utilização do `BeautifulSoup4` para navegar na árvore DOM e isolar tabelas de estatísticas.
* **Segurança:** Gerenciamento de credenciais sensíveis via variáveis de ambiente (`.env`).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12+
* **Bibliotecas:** * `discord.py` (Interface do Bot)
    * `beautifulsoup4` (Parsing de HTML)
    * `requests` (Requisições HTTP)
    * `python-dotenv` (Segurança de dados)

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório
```bash
git clone [https://github.com/julianpbarbosa/lol-counter-picker-scraper.git](https://github.com/julianpbarbosa/lol-counter-picker-scraper.git)
cd lol-counter-picker-scraper
import os
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import unicodedata
from dotenv import load_dotenv  # Importante para segurança

# Carrega as variáveis de ambiente do arquivo .env (Onde está sua senha segura)
load_dotenv()

# Configuração dos Intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def formatar_nome_campeao(nome: str) -> str:
    """
    Normaliza o nome do campeão para o formato de URL (slug).
    Exemplo: 'Renata Glasc' -> 'renata', 'Wukong' -> 'monkeyking'
    """
    # Remove acentos e caracteres especiais
    n = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')
    # Remove espaços, pontos e apóstrofos e deixa minúsculo
    n = n.lower().replace(" ", "").replace("'", "").replace(".", "")
    
    # Tratamento de exceções conhecidas do League of Graphs
    excecoes = {
        "wukong": "monkeyking",
        "renataglasc": "renata",
        "drmundo": "drmundo",
        "nunu&willump": "nunu",
        "nunu": "nunu"
    }
    
    return excecoes.get(n, n)

def buscar_dados_log(champ: str, sub_url: str = "builds"):
    """
    Realiza a requisição HTTP (Scraping) no site League of Graphs.
    Retorna o objeto BeautifulSoup ou None em caso de erro.
    """
    champ_slug = formatar_nome_campeao(champ)
    url = f"https://www.leagueofgraphs.com/pt/champions/{sub_url}/{champ_slug}"
    
    # Headers são essenciais para simular um navegador real e evitar bloqueio 403
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9",
        "Referer": "https://www.google.com/"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            print(f"Erro: Status Code {response.status_code}")
            return None
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None

@bot.event
async def on_ready():
    print(f'🤖 Bot conectado como {bot.user}')

@bot.command()
async def counters(ctx, *, champ):
    """
    Comando !counters [nome]. Busca os piores matchups do campeão.
    """
    await ctx.send(f"🛡️ **Analisando dados para {champ}...**")
    
    soup = buscar_dados_log(champ, sub_url="counters")
    
    if not soup:
        await ctx.send(f"❌ Não encontrei o campeão **{champ}**. Verifique a digitação.")
        return
        
    try:
        counters_list = []
        tabelas = soup.find_all("table", class_="data_table")
        
        tabela_alvo = None
        
        # Lógica para encontrar a tabela correta de "Piores contra"
        for tab in tabelas:
            prev = tab.find_previous(["h3", "h2", "div"])
            if prev and any(x in prev.text for x in ["Piores", "Worst"]):
                tabela_alvo = tab
                break
        
        # Fallback: Se não achar pelo título, tenta pegar a segunda tabela da página
        if not tabela_alvo and len(tabelas) > 1:
            tabela_alvo = tabelas[1]
            
        if tabela_alvo:
            # Pega apenas os 5 primeiros resultados para não poluir o chat
            for row in tabela_alvo.find_all("tr")[1:6]:
                nome = row.find("span", class_="name")
                if nome: 
                    counters_list.append(nome.text.strip())
        
        if counters_list:
            # Cria um Embed bonito (Visualização de Dados)
            embed = discord.Embed(
                title=f"☠️ Melhores Counters contra {champ.capitalize()}",
                description="Estatisticamente, estes campeões têm maior taxa de vitória contra ele(a):",
                color=0xe74c3c 
            )
            # Adiciona os nomes com formatação de lista
            embed.add_field(name="Campeões", value="\n".join([f"• {c}" for c in counters_list]), inline=False)
            embed.set_footer(text="Dados extraídos de LeagueOfGraphs")
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("⚠️ Erro na extração: A estrutura da página mudou ou não há dados suficientes.")
            
    except Exception as e:
        await ctx.send(f"❌ Erro interno no processamento de dados: `{e}`")

# Pega o token do arquivo .env (Seguro)
bot.run(os.getenv("DISCORD_TOKEN"))
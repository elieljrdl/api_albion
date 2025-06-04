import requests
import json
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt

def coleta_nome_item():
    resposta = requests.get('https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.json')

    json_conteudo = resposta.json()
    dados = []
    for i in json_conteudo:
        id_item = i['Index']
        nome_item = i['UniqueName']
        
        try:
            pt_br = i['LocalizedNames']['PT-BR']
            en_us = i['LocalizedNames']['EN-US']
        except:
            pt_br = None
            en_us = None
            
        dados.append({
            'id': int(id_item),
            'nome': nome_item,
            'pt-br': pt_br,
            'en-us': en_us,
            })
        
    
    return dados


def preco_gold_hoje():
    hoje = date.today()
    
    url = f'https://old.west.albion-online-data.com/api/v2/stats/Gold?date={hoje}'
    resposta = requests.get(url)
    
    dados_preco = []
    
    horarios = [datetime.fromisoformat(i['timestamp']) for i in resposta.json()]
    precos = [i['price'] for i in resposta.json()]
    
    plt.figure(figsize=(12,6))
    plt.plot(horarios, precos, marker='o', linestyle='-')
    plt.title(f'Preço em {hoje}')
    plt.xlabel('Horário')
    plt.ylabel('Preço')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
        


preco_gold_hoje()
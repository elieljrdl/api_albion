import requests
import json

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


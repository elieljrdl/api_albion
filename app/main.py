from busca_item import coleta_nome_item
from db import engine, SessionLocal
from models import Base, Item
 
nome_itens = coleta_nome_item()

def iniciar_banco():
    Base.metadata.create_all(bind=engine)

def adicionar_item_banco(id, nome, pt_br, en_us):
    db = SessionLocal()
    novo_item = Item(id=id, nome=nome, pt_br=pt_br, en_us=en_us)
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    db.close()
    return novo_item

if __name__ == '__main__':
    iniciar_banco()
    
    for i in nome_itens:
       adicionar_item_banco(i['id'], i['nome'], i['pt-br'], i['en-us'])

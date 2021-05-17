import json
from fastapi import FastAPI

app = FastAPI()

with open("dados.json") as json_file:
    dados = json.load(json_file)

proposicoes = dados['dados']

@app.get('/proposicoes')
def listar_todas_proposicoes():
    return proposicoes

@app.get('/autor/{autor_prop}')
def listar_propoicoes_autor(autor_prop:str):
    prop_autor = []
    find = False

    for proposicoes in dados['dados']: # lista de proposições
        for autores in proposicoes['autores']: # lista de autores por
            if(autores['nomeAutor']  == autor_prop):
                find = True
                prop_autor.append(proposicoes)

    if(find):        
        return prop_autor
    else:
        return {"Erro": "Autor não encontrado!"}

@app.get('/tipo/{tipo_prop}')
def listar_proposicoes_tipo(tipo_prop:str):
    prop_tipo = []
    find = False

    for proposicao in dados['dados']:
        if(proposicao['descricaoTipo'] == tipo_prop):
            find = True
            prop_tipo.append(proposicao)

    if(find):        
        return prop_tipo
    else:
        return {"Erro": "Expressão mal formulada!"}
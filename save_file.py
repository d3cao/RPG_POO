import json
import os
import personagem

def persons_dict(personagem):
    return {
        'Classe': personagem.__class__.__name__,
        'Nome': personagem.nome,
        'Role': personagem.role,
        'Vida': personagem.vida,
        'Dano': personagem.dano,
        'Experiência': personagem.xp
    }

def verify(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return False
    
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return bool(dados)
    except json.JSONDecodeError:
        return False
    
def load(caminho_arquivo, lista_personagens):
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            try:
                dados = json.load(arquivo)
            except json.JSONDecodeError:
                dados = []
    else :
        dados = []

    for indice in dados:
        nome = indice['Nome']
        role = indice['Role']
        vida = indice['Vida']
        dano = indice['Dano']
        xp = indice['Experiência']

        p = personagem.personagem(vida, dano, nome, xp, role)

        lista_personagens.append(p)
    

def salvar_json(lista_personagens, nome_arquivo):
    dados = [persons_dict(p) for p in lista_personagens]

    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
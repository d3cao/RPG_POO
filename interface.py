import personagem
import os
import save_file

player = None
personagens = []

def salvar():
     save_file.salvar_json(personagens, 'personagens.json')

def exit():
    os.system('clear')
    print('Finalizando programa...')

def retorno():
        print()
        input('Digite uma tecla para voltar para o menu: ')
        main()

def definir_classe(nome):
    print('Qual a classe do personagem: ')
    print('1-Guerreiro')
    print('2-Mago')
    print('3-Arqueiro')
    a = input()
    classes = {
        '1': personagem.guerreiro(nome),
        '2': personagem.mago(nome),
        '3': personagem.arqueiro(nome)
    }
    return classes.get(a)

def criacao_personagem():
    global player
    os.system('clear')
    nome = input('Qual o nome do seu personagem ? ')
    player = definir_classe(nome)
    personagens.append(player)
    print('Personagem criado com sucesso!')
    retorno()

def ficha():
    os.system('clear')
    print('Ficha Personagem :')
    player.ficha()
    retorno()

def interface():
    os.system('clear')
    print('_________Seja bem vindo!_________')
    print()
    print('(1) Criação de personagem')
    print('(2) Ficha do personagem')
    print('(3) Salvar os personagens')
    print('(4) Finalizar programa')
    entry = input('Digite a opção desejada: ')
    opcoes = {
        '1': criacao_personagem,
        '2': ficha,
        '3': salvar,
        '4': exit
    }
    escolhida = opcoes.get(entry)
    if escolhida:
        escolhida()
    else :
        print('opção invalida')
    '''
    if entry == '1':
        criacao_personagem()
    elif entry == '2':
        ficha()
    elif entry == '3':
        exit()
    '''

def main():
    interface()
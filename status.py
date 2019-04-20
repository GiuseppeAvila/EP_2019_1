# -*- coding: utf-8 -*-

import json

def cria_personagem_inicial():
    with open("Dialogo inicial narrador.txt","r",encoding = "utf8") as dialogo:
        texto = dialogo.read()
    print (texto)
    nome = input("...seu Nome é?  ")
    print()
    print("----------------")
    print()
    print("Ótimo! Agora {0}, vamos descobrir o que temos dentro de você!".format(nome))
    print()
    print("Vamos fazer o seguinte, escolha uma classe e um background e eu faço isso ser verdade, eu sou incrível não é mesmo?")
    print()
    
    # IMPLEMENTANDO SISTEMA DE CRIAÇÃO DE PERSONAGEM:
    classe_jogador = escolha_classe()
    background_jogador = escolha_background()
    
    print()
    print("Tudo pronto para começarmos...")
    print()
    print("Opa, parece que chegamos!....")
    print()
    print("=======================")
    print()    
    
    return classe_jogador,background_jogador

def escolha_classe():
    with open("classes.json") as classes:
        classes_disponiveis = json.load(classes)
    a = str(classes_disponiveis.keys())
    a = a[11:]
    a = a[:-2]
    a = a.replace("'", "")
    a = a.replace(" ", "")

    # a são as classes na forma de str
    # b são as classes na forma de lista
    
    b = a.split(",")

    
    escolheu_classe = False
    while not escolheu_classe:
        print("As classes são...{}".format(a))
        print("Deseja saber mais sobre alguma delas ou quer já escolher?")
        print()
        print("Quero ser um [M]ago")
        print("Quero ser um [L]adino")
        print("Quero ser um L[u]tador")
        print("Quero [s]aber mais...")
        escolha1 = input()
        opcoes = ["M", "L", "U"]
        if escolha1.upper() in opcoes:
            print()
            print("{0} - Essa é a sua escolha? [S]im / [N]ão".format(b[opcoes.index(escolha1.upper())]))
            confirmacao = input()
            if confirmacao.upper() == "S":
                classe_jogador = b[opcoes.index(escolha1.upper())]
                print()
                print("Sua classe é {0}".format(classe_jogador))
                print()
                escolheu_classe = True
                return classe_jogador
            elif confirmacao.upper() == "N":
                print()
                print("Se decida")
                print()
            else:
                print("Escolha inválida")
        elif escolha1.upper() == "S":
            print()
            print("O Mago tem...")
        else:
            print("Escolha inválida")

def escolha_background():
    with open("backgrounds.json") as backgrounds:
        backgrounds_disponiveis = json.load(backgrounds)
    c = str(backgrounds_disponiveis.keys())
    c = c[11:]
    c = c[:-2]
    c = c.replace("'","")
    c = c.replace(" ", "")
    
    # c são os backgrounds na forma de str
    # d são os backgrounds na forma de lista
    
    d = c.split(",")
    
    escolheu_background = False
    while not escolheu_background:
        print("Os backgrounds são...{}".format(c))
        print("Deseja saber mais sobre algum deles ou quer já escolher?")
        print()
        print("Quero ser um [A]ristocrata")
        print("Quero ser um [E]sportista")
        print("Quero ser um [G]amer")
        print("Quero [s]aber mais...")
        escolha1 = input()
        opcoes = ["A", "E", "G"]
        if escolha1.upper() in opcoes:
            print()
            print("{0} - Essa é a sua escolha? [S]im / [N]ão".format(d[opcoes.index(escolha1.upper())]))
            confirmacao = input()
            if confirmacao.upper() == "S":
                background_jogador = d[opcoes.index(escolha1.upper())]
                print()
                print("Seu background é {0}".format(background_jogador))
                print()
                escolheu_background = True
                return background_jogador
            elif confirmacao.upper() == "N":
                print()
                print("Se decida")
                print()
            else:
                print("Escolha inválida")
        elif escolha1.upper() == "S":
            print()
            print("O Aristocrata tem...")
        else:
            print("Escolha inválida")
            
cria_personagem_inicial()

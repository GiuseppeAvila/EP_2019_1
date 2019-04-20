# -*- coding: utf-8 -*-

#import json

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
    print("Vamos fazer o seguinte, escolha uma classe e um background...")
    print("...e eu faço isso ser verdade, eu sou incrível não é mesmo?")
    print()
    
    '''
    IMPLEMENTANDO SISTEMA DE CRIAÇÃO DE PERSONAGEM:
    
    with open("classes.json") as classes:
        classes_disponiveis = json.load(classes)
    a = str(classes_disponiveis.keys())
    a = a[11:]
    a = a[:-2]
    a = a.replace("'","")
    
    # a são as classes na forma de str
    # b são as classes na forma de lista
    
    #b = a.split(",")
    #print(b)
    
    print("As classes são...{}".format(a))
    print("Deseja saber mais sobre alguma delas ou quer já escolher?")
    print()
    print("escolher")
    print("saber")
    escolha1 = input("Eu gostaria de...")
        
    
    with open("backgrounds.json") as backgrounds:
        backgrounds_disponiveis = json.load(backgrounds)
    c = str(backgrounds_disponiveis.keys())
    c = c[11:]
    c = c[:-2]
    c = c.replace("'","")
    
    # c são os backgrounds na forma de str
    # d são os backgrounds na forma de lista
    
    #d = c.split(",")
    #print(b)
    
    print("Os backgrounds são...{}".format(c))
    
    '''
    
    print()
    print("Tudo pronto para começarmos...")
    print()
    print("Opa, parece que chegamos!....")
    print()
    print("=======================")
    print()    
    
#cria_personagem_inicial()
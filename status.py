# -*- coding: utf-8 -*-
#              Sistema de combate! Que a batalha comece!
import json

def cria_personagem_inicial():
    with open("Dialogo inicial narrador.txt","r",encoding = "utf8") as dialogo:
        texto = dialogo.read()
    print (texto)
    #nome = input("...seu Nome é?  ")
    print()
    print("----------------")
    print()
    print("Ótimo! Agora {0}, vamos descobrir o que temos dentro de você!".format("nome"))
    print()
    print("Vamos fazer o seguinte, escolha uma classe e um background...")
    print("...e eu faço isso ser verdade, eu sou incrível não é mesmo?")
    print()

    with open("classes.json") as classes:
        classes_disponiveis = json.load(classes)
    a = str(classes_disponiveis.keys())
    a = a[11:]
    a = a[:-2]
    a = a.replace("'","")
    #b = a.split(",")
    #print(a)
    #print(b)
    print("As classes são...{}".format(a))
    
    print()
    print("Tudo pronto para começarmos...")
    print()
    print("Opa, parece que chegamos!....")
    print()
    print("=======================")
    print()    
    
cria_personagem_inicial()
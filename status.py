# -*- coding: utf-8 -*-
#              Sistema de combate! Que a batalha comece!

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
    print("Vamos fazer o seguinte, distribua 25 pontos em quais quiser e eu faço isso ser verdade, eu sou incrível não é mesmo?")
    print()
    print("As habilidades são...inteligencia, carisma, agilidade, destreza e sorte:")
    print()
    pontos_corretos = False
    while not pontos_corretos:
        pontos = 25
        print("Seus pontos atuais são: {}".format(pontos))
        
        inteligencia = int(input("Inteligencia: "))
        pontos -= inteligencia
        print()
        print("Seus pontos atuais são: {}".format(pontos))

        carisma = int(input("Carisma: "))
        pontos -= carisma
        print()
        print("Seus pontos atuais são: {}".format(pontos))
        
        
        agilidade = int(input("Agilidade: "))
        pontos -= agilidade
        print()
        print("Seus pontos atuais são: {}".format(pontos))

        destreza = int(input("Destreza: "))
        pontos -= destreza
        print()
        print("Seus pontos atuais são: {}".format(pontos))

        sorte = int(input("Sorte: "))
        print()
        soma = inteligencia + carisma + agilidade + destreza + sorte
        
        if soma > 25:
            print("Aaaaaa não sabe contar? São 25 pontos de habilidade!")
        elif soma < 25:
            print("Aaaaaa não sabe contar? São 25 pontos de habilidade!")
        else:
            pontos_corretos = True
    maior = 0
    lista = [inteligencia,carisma,agilidade,destreza,sorte] 
    lista_hab = ["inteligencia","carisma","agilidade","destreza","sorte"]
    for i in range(len(lista)):
        if maior < lista[i]:
            maior = lista[i]
            maior_habilidade = lista_hab[i]
    if maior == lista[0] and maior == lista[1] and maior == lista[2] and maior == lista[3] and maior == lista[4]:
        maior_habilidade = "de tudo"
    print("Beleza, bastante {}, hein? Tudo pronto para começarmos...".format(maior_habilidade))
    print()
    print("Opa, parece que chegamos!....")
    print()
    print("=======================")
    print()    
# -*- coding: utf-8 -*-
import random

#def lutar():
    
    
    
def fugir(personagem, opcoes):
    print("Só corre!")
    
    AGI = personagem["Status"]["AGI"]
    numero = random.randint(0, 100)
    
    if numero >= (20 - AGI):
        print("Toma essa monstrengo! Você escapou!")
        print()
        em_batalha = False
        print("=======================")
        for i,j in opcoes.items():
            print()
            print(i,"=",j)
                    
    else:
        print("Puts ele previu seus movimentos! Não foi dessa vez!")
        print()
        em_batalha = True
    
    return em_batalha

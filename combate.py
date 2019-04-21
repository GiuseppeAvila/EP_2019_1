# -*- coding: utf-8 -*-
import random
import json
from pprint import pprint

#def lutar():
    
    
    
def fugir(personagem, opcoes):
    print("Só corre!")
    
    AGI = personagem["Status"]["AGI"]
    numero = random.randint(0, 100)
    
    if numero >= (20 - AGI):
        print("Toma essa monstrengo! Você escapou!")
        print()
        monstro_vivo = False
        print("=======================")
        for i,j in opcoes.items():
            print()
            print(i,"=",j)
                    
    else:
        print("Puts ele previu seus movimentos! Não foi dessa vez!")
        print()
        monstro_vivo = True
    
    return monstro_vivo

def monstro_cenario(monstro):
    with open("bestiario.json") as bestiario:
        bestas = json.load(bestiario)
            
        monstro_atual = {monstro :
                
                {"Tipo" : [],
                 
                 "HP_Max" : 0,
                 "HP_atual": 0,
                 
                 "PP_Max" : 0,
                 "PP_Atual": 0,
                 
                 "F_ATK" : 0,
                 "P_ATK" : 0,
                 
                 "F_DEF" : 0,
                 "P_DEF" : 0,
                 
                 "AGI" : 0,
                 
                 "Habilidades" : []
                 }
                }
            
        lista_tipo_monstro = bestas[monstro]["Tipo"]
        for a in range(len(lista_tipo_monstro)):
            monstro_atual[monstro]["Tipo"].append(lista_tipo_monstro[a])
            
        monstro_atual[monstro]["HP_Max"] = bestas[monstro]["HP_Max"]
        monstro_atual[monstro]["HP_atual"] = bestas[monstro]["HP_Max"]
            
        monstro_atual[monstro]["PP_Max"] = bestas[monstro]["PP_Max"]
        monstro_atual[monstro]["PP_Atual"] = bestas[monstro]["HP_Max"]
            
        monstro_atual[monstro]["F_ATK"] = bestas[monstro]["F_ATK"]
        monstro_atual[monstro]["P_ATK"] = bestas[monstro]["P_ATK"]
            
        monstro_atual[monstro]["F_DEF"] = bestas[monstro]["F_DEF"]
        monstro_atual[monstro]["P_DEF"] = bestas[monstro]["P_DEF"]
            
        monstro_atual[monstro]["AGI"] = bestas[monstro]["AGI"]
            
        lista_hab_monstro = bestas[monstro]["Habilidades"]
        for m in range(len(lista_hab_monstro)):
            monstro_atual[monstro]["Habilidades"].append(lista_hab_monstro[m])
            
        pprint(monstro_atual)
        return monstro_atual
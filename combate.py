# -*- coding: utf-8 -*-
import random
import json
from pprint import pprint

#def lutar():
    
    
    
def fugir(personagem, opcoes):
    print("Só corre!")
    
    AGI = personagem["Status"]["AGI"]
    #numero = random.randint(0, 100)
    numero = 1
    
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
    with open("bestiario.json", encoding="utf8") as bestiario:
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
                 
                 "Premios" : {}
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
            
        dicionario_premios_monstro = bestas[monstro]["Premios"]
        for chave,valor in dicionario_premios_monstro.items():
        
            if chave in monstro_atual[monstro]["Premios"]:
                monstro_atual[monstro]["Premios"][chave] += valor
        
            elif chave not in monstro_atual[monstro]["Premios"]:
                monstro_atual[monstro]["Premios"][chave] = valor
            
        print()
        print(bestas[monstro]["Descrição"])
        print()
        pprint(monstro_atual)
        return monstro_atual
    
def usar(personagem, item_escolhido):
    
    itens_usaveis = ["Poção de Cura"]
    
    if item_escolhido in itens_usaveis:
        if item_escolhido == "Poção de Cura":
            personagem["Inventario"]["Poção de Cura"] -= 1
            cura = 5
            personagem["Status"]["HP_Atual"] += cura
            if personagem["Status"]["HP_Atual"] > personagem["Status"]["HP_Max"]:
                personagem["Status"]["HP_Atual"] = personagem["Status"]["HP_Max"]
            print()
            print("Você se sente revitalizado... como se {}HP tivessem sido restaurados!".format(cura))
            print("Sua vida neste momento é {}".format(personagem["Status"]["HP_Atual"]))
            print()
    
    else:
        print("Esse item não tem ação em combate...mas talvez sirva para outra coisa...")
        print()
        
    return personagem
    
'''                                              
    elif item_escolhido == "Coisa":
        personagem["Inventario"]["Coisa"] -= 1
'''
def I(personagem):
    print("Itens em seu inventario, escolha um deles!")
    for f,g in personagem["Inventario"].items():
        print()
        print(f,"=",g)
    escolhendo_item = True
    while escolhendo_item:
        print()
        print("voltar = Voltar para as escolhas de combate")
        print()
        print("Dê o Nome do Item que deseja usar:")
        item_escolhido = input()
        if item_escolhido in personagem["Inventario"]:
            personagem = usar(personagem, item_escolhido)
            escolhendo_item = False
            menu_atk = False
        elif item_escolhido == "voltar":
            print()
            print("Take your time:")
            print("[A]tacar / [P]sy / [D]efender / [I]tem / [G]un / [S]tatus")
                    
            acao = input()
            acao = acao.upper()
            print()
            escolhendo_item = False
            menu_atk = True
        else:
            print("Você não possui esse item")
            print()
            print("Itens em seu inventario, escolha um deles!")
            for f,g in personagem["Inventario"].items():
                print()
                print(f,"=",g)
    return menu_atk
    #return personagem         

def A(personagem,monstro_atual,opcoes):
    
    F_ATK_personagem = personagem["Status"]["F_ATK"]
    
    F_DEF_monstro = monstro_atual["F_DEF"]
    
    dano_recebido = F_ATK_personagem - F_DEF_monstro*0.3
    
    if dano_recebido < 0:
        dano_recebido = 0
        
    monstro_atual["HP_atual"] -= dano_recebido
    
    if monstro_atual["HP_atual"] <= 0:
        monstro_atual["HP_atual"] = 0
        
        monstro_vivo = False
        
        print("Monstrengo eliminado!")
                                    
        premios = monstro_atual["Premios"]

        print("Você encontrou em sua carcaça.. {}".format(premios))
        print()
                                    
        for chave,valor in premios.items():
        
            if chave in personagem["Inventario"]:
                personagem["Inventario"][chave] += valor
        
            elif chave not in personagem["Inventario"]:
                personagem["Inventario"][chave] = valor
                
    elif monstro_atual["HP_atual"] > 0:
        monstro_vivo = True
                                          
    print("Você deu incríveis {} de dano!".format(dano_recebido))
    
    if monstro_atual["HP_atual"] > 0:
        print("A vida do monstro atualmente é: {}".format(monstro_atual["HP_atual"]))
                                
    if not monstro_vivo:
        print()
        print("=======================")
        for i,j in opcoes.items():
            print()
            print(i,"=",j)
        print()
            
    return monstro_vivo 

def P(personagem,monstro_atual,opcoes):
    
    P_ATK_personagem = personagem["Status"]["P_ATK"]
        
    P_DEF_monstro = monstro_atual["P_DEF"]
        
    dano_recebido = P_ATK_personagem - P_DEF_monstro*0.3
        
    if dano_recebido < 0:
        dano_recebido = 0
            
    personagem["Status"]["PP_Atual"] -= 5
        
    if personagem["Status"]["PP_Atual"] < 0:
        personagem["Status"]["PP_Atual"] = 0
            
    monstro_atual["HP_atual"] -= dano_recebido
        
    if monstro_atual["HP_atual"] <= 0:
        monstro_atual["HP_atual"] = 0
        
        monstro_vivo = False
            
        print("Monstrengo eliminado!")
                                    
        premios = monstro_atual["Premios"]
            
        print("Você encontrou em sua carcaça.. {}".format(premios))
        print()
                                    
        for chave,valor in premios.items():
                
            if chave in personagem["Inventario"]:
                personagem["Inventario"][chave] += valor
                
            elif chave not in personagem["Inventario"]:
                personagem["Inventario"][chave] = valor
                
    elif monstro_atual["HP_atual"] > 0:
        monstro_vivo = True
                                            
    print("Você deu incríveis {} de dano!".format(dano_recebido))
            
    if monstro_atual["HP_atual"] > 0:
        print("A vida do monstro atualmente é: {}".format(monstro_atual["HP_atual"]))
                                
    if not monstro_vivo:
        print()
        print("=======================")
        for i,j in opcoes.items():
            print()
            print(i,"=",j)
        print()
                    
    return monstro_vivo
                       
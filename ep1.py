# -*- coding: utf-8 -*-
'''
            EP 2019-1: Escape Insper

 Alunos: 3
 - aluno A: Daniel Terra danielgt1@al.insper.edu.br
 - aluno B: Fernando Giuseppe, fernandogab@al.insper.edu.br
 - aluno C: Erick Finger, erickf1@al.insper.edu.br

'''

import status
import carregar_cenarios
import random
import combate
import json
#import supreme_weapons as sw

def main():
    
    #  Situação inicial, e criação de personagem
    cenarios_conhecidos = ["inicio"]
    carregar_cenarios.situacao()
    cenario, nome_cenario_atual = carregar_cenarios.carregar_cenarios()
    personagem = status.personagem_protagonista()
    habilidade1 = personagem["Status"]["Habilidades"][0]
    habilidade2 = personagem["Status"]["Habilidades"][1]
    print("Suas habilidades são {0} e {1}".format(habilidade1, habilidade2))
    print()
    with open("habilidades.json","r", encoding="utf8") as habs:
        habs = json.load(habs)
    print(habilidade1 , " : " , habs[habilidade1]["Descrição"])
    print(habilidade2 , " : " , habs[habilidade2]["Descrição"])
    print()
    
    #  Funcionando o jogo
    venceu_jogo = False
    game_over = False
    while not game_over:
        #  Carrega o dicionario do cenario atual
        cenario_atual = cenario[nome_cenario_atual]
        carregar_cenarios.inicio(cenario_atual)
        
        #  Cenários conhecidos para o teleporte
        if nome_cenario_atual not in cenarios_conhecidos:
            cenarios_conhecidos.append(nome_cenario_atual)
            
        # Ocorrencia de monstro
        em_batalha = False
        lista_monstro_atual = cenario_atual["inimigos"]
        n = random.randint(0,(len(lista_monstro_atual)-1))
        monstro = lista_monstro_atual[n]
        
        chance_monstro = random.randint(0,15)
        #  Para testar batalha:
        #chance_monstro = 0
            
        if chance_monstro == 0:
            em_batalha = True
            if monstro == "Mega Ayres":
                combate.final_boss()
            if monstro == "Alan-Tron 3000":
                print()
                print("Você vê o Alan olhando pela janela da sala")
                print()
                print("Há algo errado...")
                print("Cabos e circuitos elétricos cobrem o corpo dele")
                print()
                print("Ele se vira pra você e diz:")
                print("I NEED TO KILL SARAH CONNOR")
                print()
                print("Ele foi possuído por um elemental!")
                print()
                    
        else:
            em_batalha = False
        
        if em_batalha:
            print("=======================")
            print()
            print("Apareceu um {} no seu caminho! Ele quer acabar com você!".format(monstro))
        
        print()
        print("=======================")
        
        #  Opções aparecer na tela 
        opcoes = cenario_atual['opcoes']
        if not em_batalha:
            for i,j in opcoes.items():
                print()
                print(i,"=",j)
            
        #  Morte da personagem por falta de opções
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        
        #  Possui opções, faz uma escolha
        elif em_batalha:
            
             #Implementação dos valores desse monstro:
            monstro_atual = combate.monstro_cenario(monstro)
            monstro_atual = monstro_atual[monstro]
            monstro_vivo = True

            escolha = ""
            i = 0
            
            #  Enquanto o monstro não morrer
            while monstro_vivo:
                
                monstro_vivo = combate.discucao_fisica(personagem,monstro_atual,opcoes,i)
                print("====================")  
                print()
                n_morreu = combate.monstrengo(monstro_atual,personagem)
                print("====================")  
                print()
                if personagem["Status"]["HP_Atual"] <= 0:
                    game_over = True
                    break
                if n_morreu == False:
                    game_over = True
                    break
                if monstro == "Mega Ayres" and (not monstro_vivo):
                   game_over = True
                   venceu_jogo = True
                   break
        #  Se escolher um local e não estiver em batalha
        else:
            print()
            print("====================")
            escolha = input("O que deseja fazer? ")
            
           #  Se a escolha estiver dentre as disponíveis e for um local == ir para lá
            if escolha in opcoes:
                if escolha == "comprar algo":
                    personagem = carregar_cenarios.compra(personagem, opcoes)
                elif escolha == "aluno":
                    print()
                    with open("dialogos_genericos.json", "r", encoding="utf8") as conversa:
                        falas = json.load(conversa)
                    num_falas = falas.values()
                    num_falas = list(num_falas)
                    lista_falas = num_falas[0]
                    
                    n = random.randint(0, len(lista_falas)-1)
                    print(lista_falas[n])
                    print()
                    print("--------------------")
                    print()
                else:
                    nome_cenario_atual = escolha
                    print()
                    print("====================")
            
            #  Se a escolha não estiver dentre as disponíveis == perguntar novamente
            else:
                print("<suspiro> Eu preciso te explicar tudo? O que você escolheu não é uma opção válida, atenha-se às opções apresentadas! Ou o quê, você acha que consegue atravessar paredes?")
                print()
                print("====================")
                continue

    if venceu_jogo:
        print("Parabéns você venceu, o seu professor evaporou no éter")
        print("Você não precisa mais entregar o EP!")
        print()
        print("Você foi preso por atomizar o seu professor!")
        print()
        print("PARABÉNS!!!")
        print()
        print("OBS: se você tivesse feito o EP em vez de embarcar em uma Odisséia....")
        print()
        print("----------------------------------THE END----------------------------------")
    else:
        print("Você morreu!")

#  Programa principal.
if __name__ == "__main__":
    main()

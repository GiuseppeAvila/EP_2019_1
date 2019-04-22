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
from pprint import pprint
#import supreme_weapons as sw

def main():
    
    #  Situação inicial, e criação de personagem
    cenarios_conhecidos = ["inicio"]
    carregar_cenarios.situacao()
    cenario, nome_cenario_atual = carregar_cenarios.carregar_cenarios()
    personagem = status.personagem_protagonista()
    
    #  Funcionando o jogo
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
        
        #chance_monstro = random.randint(0,1)
        #  Para testar batalha:
        chance_monstro = 0
            
        if chance_monstro == 0:
            em_batalha = True
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
                
                # Escolha de batalha
                print("[L]utar / [F]ugir ")
                escolha_bat = input()
                escolha_bat = escolha_bat.upper()
                
                #  Personagem Lutando!
                if escolha_bat == "L":
                    
                    #em_batalha = combate.lutar(personagem) 
                    print()
                    print("Take your time:")
                    print("[A]tacar / [P]sy / [D]efender / [I]tem / [G]un / [S]tatus")
                    
                    acao = input()
                    acao = acao.upper()
                    acoes_possiveis = ["A","P","D","I","G","S"]
                    print()
                    
                    menu_atk = True
                    while menu_atk:
                        
                        if acao in acoes_possiveis:
                            if acao == "A":
                                monstro_vivo = combate.A(personagem,monstro_atual,opcoes)
                                menu_atk = False

                            elif acao == "S":
                                pprint(personagem)
                                print()
                                print("Take your time:")
                                print("[A]tacar / [P]sy / [D]efender / [I]tem / [G]un / [S]tatus")
                    
                                acao = input()
                                acao = acao.upper()
                                print()
                                menu_atk = True
                                
                            elif acao == "P":
                                
                                if personagem["Status"]["PP_Atual"] >= 5:
                                    monstro_vivo = combate.P(personagem,monstro_atual,opcoes)
                                    menu_atk = False
                                
                                else:
                                    print("Seu PP está baixo, precisa-se de 5PP para realizar um PP ATK!")
                                    print()
                                    print("Take your time:")
                                    print("[A]tacar / [P]sy / [D]efender / [I]tem / [G]un / [S]tatus")
                    
                                    acao = input()
                                    acao = acao.upper()
                                    print()
                                    menu_atk = True

                            elif acao == "D":
                                #F_guard = 0.5*personagem["Status"]["F_DEF"]
                                #P_guard = 0.5*personagem["Status"]["P_DEF"]
                                menu_atk = False
                            
                            elif acao == "I":
                                menu_atk = combate.I(personagem)
                                
                            elif acao == "G":
                                print("Essa ação ainda não foi implementada - volte a escolher")
                                print()
                                print("Take your time:")
                                print("[A]tacar / [P]sy / [D]efender / [I]tem / [G]un / [S]tatus")
                    
                                acao = input()
                                acao = acao.upper()
                                print()
                                menu_atk = True
                        else:
                            print("Você ataca com {}! É super efetivo!".format(acao))
                            print()
                            print()
                            print("Com isso você causa fenomenais 0 de dano, já que {} não é uma opção válida".format(acao))
                            print("Para de bancar o espertinho e aprenda a jogar")
                            print()
                            print("Escolha uma opção abaixo.. e lembre-se, tome o tempo que precisar!")
                            print()
                            print("Take your time:")
                            print("[A]tacar / [P]sy / [D]efender / [I]tem / [G]un / [S]tatus")
                    
                            acao = input()
                            acao = acao.upper()
                            print()
                            menu_atk = True
                        
                #  Fuga da personagem quando em batalha
                elif escolha_bat == "F":
                    if i > 0:
                        print("Você já tentou fugir e não deu, agora se vira, acaba com ele")
                        continue
                    else:
                        monstro_vivo = combate.fugir(personagem, opcoes)
                        i+=1

                        
                        
                elif monstro_atual["HP_atual"] <= 0:
                    monstro_vivo = False
                
                else:
                    print("Não seja covarde!")
                    monstro_vivo = True
                
        #  Se escolher um local e não estiver em batalha
        else:
            print()
            print("====================")
            escolha = input("O que deseja fazer? ")
            
            #  Se a escolha estiver dentre as disponíveis e for um local == ir para lá
            if escolha in opcoes:
                if escolha == "comprar algo":
                    personagem = carregar_cenarios.compra(personagem, opcoes)
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

    print("Você morreu!")

#  Programa principal.
if __name__ == "__main__":
    main()

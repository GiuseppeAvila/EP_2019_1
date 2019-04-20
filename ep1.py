'''
            EP 2019-1: Escape Insper

 Alunos: 3
 - aluno A: Daniel Terra danielgt1@al.insper.edu.br
 - aluno B: Fernando Giuseppe, fernandogab@al.insper.edu.br
 - aluno C: Erick Finger, erickf1@al.insper.edu.br

'''

import status
import cenarios
import random
import combate
#import supreme_weapons as sw


def main():
    
    cenarios_conhecidos = ["inicio"]
    
    # Situação inicial, e criação de personagem
    cenarios.situacao()
    status.cria_personagem_inicial()
    cenario, nome_cenario_atual = cenarios.carregar_cenarios()
    
    # Funcionando o jogo
    game_over = False
    while not game_over:
        
        cenario_atual = cenario[nome_cenario_atual]
        
        cenarios.inicio(cenario_atual)
        
        #  Cenários conhecidos para o teleporte
        if nome_cenario_atual not in cenarios_conhecidos:
            cenarios_conhecidos.append(nome_cenario_atual)
        
        print()
        print("=======================")
       
        #  Opções aparecer na tela 
        opcoes = cenario_atual['opcoes']
        for i,j in opcoes.items():
            print()
            print(i,"=",j)
            
        # Morte da personagem por falta de opções
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        
        # Possui opções, faz uma escolha
        else:
            escolha = ""
            
            #chance_monstro = random.randint(0,4)
            # para testar batalha:
            chance_monstro = 0
            
            if chance_monstro == 0:
                em_batalha = True
            else:
                em_batalha = False
            
            # Se entrar em batalha
            if em_batalha:
                
                lista_monstro_atual = cenario_atual["inimigos"]
                n = random.randint(0,(len(lista_monstro_atual)-1))
                monstro = lista_monstro_atual[n]
                
                print("Apareceu um {} no seu caminho! Ele quer acabar com você!".format(monstro))
                
                
                escolha = input("[L]utar / [F]ugir ")
    
                if escolha == "L":
                    em_batalha = combate.lutar() 
    
                elif escolha == "F":
                    em_batalha = combate.fugir()
    
                else:
                    print("Não seja covarde!")
                    escolha = input("[L]utar / [F]ugir ")
                
            # Se escolher um local e não estiver em batalha
            else:
                print()
                print("====================")
                escolha = input("O que deseja fazer? ")
            
            #Se a escolha estiver dentre as disponíveis e for um local == ir para lá
            if escolha in opcoes:
                nome_cenario_atual = escolha
                
                print()
                print("====================")
            
            #Se a escolha não estiver dentre as disponíveis == perguntar novamente
            else:
                print("<suspiro> Eu preciso te explicar tudo? O que você escolheu não é uma opção válida, atenha-se às opções apresentadas! Ou o quê, você acha que consegue atravessar paredes?")
                print()
                print("====================")
                continue

    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()

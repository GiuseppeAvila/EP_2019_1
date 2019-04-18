'''
            EP 2019-1: Escape Insper

 Alunos: 3
 - aluno A: Daniel Terra danielgt1@al.insper.edu.br
 - aluno B: Fernando Giuseppe, fernandogab@al.insper.edu.br
 - aluno C: Erick Finger, erickf1@al.insper.edu.br

'''

import status
import cenarios
#import supreme_weapons as sw


def main():
    cenarios.situacao()
    
    status.cria_personagem_inicial()
    
    cenario, nome_cenario_atual = cenarios.carregar_cenarios()

    game_over = False
    while not game_over:
        
        cenario_atual = cenario[nome_cenario_atual]
        cenarios.inicio(cenario_atual)
        
        print()
        print("=======================")
        opcoes = cenario_atual['opcoes']
        for i,j in opcoes.items():
            print()
            print(i,"=",j)
            
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""
            
            em_batalha = False
            
            if em_batalha:
                escolha = input("[L]utar / [F]ugir ")
                em_batalha = False
                
            else:
                print()
                print("====================")
                escolha = input("O que deseja fazer? ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()

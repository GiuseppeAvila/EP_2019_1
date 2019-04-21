
import json

def carregar_cenarios():
    with open("cenarios.json", "r", encoding="utf8") as arquivo:
        cenarios = json.load(arquivo)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inicio(cenario_atual):
    print(cenario_atual["título"])
    print(cenario_atual["descrição"])
    print()

def situacao():
    with open("NA HORA DO SUFOCO.txt", "r",encoding="utf8") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
    
def compra(personagem):
    em_compra = True
    while em_compra:
        produtos = {"S" : 3,
                    "P" : 3,
                    "G" : 99,
                    "T" : 1}
        print("Há uma maquina de venda automática, dentro dela tem:")
        print("[S]H 3000 - R$ 3.00")
        print("[P]SI POWER - R$ 3.00")
        print("Á[g]ua - R$ 99.00")
        print("O [T]esouro - R$ 1.00")
        print("Deseja comprar algo ou vai [e]mbora?")
        escolha1 = input().upper()
        escolhas_possiveis = ["S", "P", "G"]
        if escolha1 == "E":
            print()
            for i,j in opcoes.items():
                print()
                print(i,"=",j)
                em_compra = False
        elif escolha1 == "T":
            escolha2 = input("Tem certeza? [S]im / [N]ão").upper()
            if escolha2 == "S":
                print("Você compra O Tesouro, um pequeno baú de madeira sai da máquina")
                print("Ao abrir o baú, uma sensação de comforto e amena felicidade enche seu corpo")
                print("Você finalmente percebe que o verdadeiro tesouro não é o que está dentro deste baú,")
                print("mas sim é as amizades que você fez ao longo do caminho...")
                print("...também tem uma moeda de um real dentro do baú")
                em_compra = False
            elif escolha2 == "N":
                print("Você não tem certeza")
        elif escolha1 in escolhas_possiveis:
            checagem = personagem["Inventario"]["Dinheiro"] - produtos[escolha1]
            if checagem >= 0:
                escolha2 = input("Tem certeza? [S]im / [N]ão").upper()
                if escolha2 == "S":
                    personagem["Inventario"]["Dinheiro"] -= produtos[escolha1]
                    if escolha1 == "S":
                        personagem["Status"]["HP_Atual"] = personagem["Status"]["HP_Max"]
                        print("Você se sente revitalizado!")
                        em_compra = False
                    elif escolha1 == "P":
                        personagem["Status"]["PP_Atual"] = personagem["Status"]["PP_Max"]
                        print("Você se sente reinvigorado!")
                        em_compra = False
                    else:
                        print("Você tomou água!")
                elif escolha2 == "N":
                    print("Você não tem certeza")
                else:
                    print("Escolha invalida")
            else:
                print("Você não tem dinheiro o bastante")
        else:
            print("Escolha invalida")
        
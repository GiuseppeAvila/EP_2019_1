
import json

def carregar_cenarios():
    with open("cenarios.json", "r") as arquivo:
        cenarios = json.loads(arquivo)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inicio(cenario_atual):
    print(cenario_atual["título"])
    print(cenario_atual["descrição"])

def situacao():
    with open("NA HORA DO SUFOCO.txt", "r",encoding="utf8") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
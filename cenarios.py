def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"}
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"}
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {"inicio": "Voltar para o saguao de entrada", "fundo": "Avançar para os fundos da biblioteca"}
        },
        "garagem": {
                'título': 'Abismo, o vazio e a escuridão', 
                'descrição': 'Você está na garagem...', 
                'opcoes': {'subir elevador': 'Voltar para a superfície', 
                           'explorar': 'Ir mais ao fundo', 
                           'corredor': 'Seguir em direção aos laboratórios e ao baja'}
        },
        'rua em frente ao Insper': {
                'título': 'Os portões', 
                'descrição': 'Você saiu do Insper, está na rua', 
                'opcoes': {'predio novo': 'Entrar no prédio novo', 
                           'predio velho': 'Entrar no prédio velho', 
                           'direita': 'Seguir a rua para a direita'}
        },
        'saboroso': {
                'título': 'El flavors', 
                'descrição': 'Você está no restaurante da esquina', 
                'opcoes': {'comer': 'Gastar R$19.9999999999999999... e recuperar X de HP!', 
                           'beber agua': 'Retornar sua adrenalina em X%! Apenas R$3!', 
                           'conversar com Daniel Guzzo': 'Daniel?'}
        }
    }

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inicio(cenario_atual):
    print(cenario_atual["titulo"])
    print(cenario_atual["descricao"])

def situacao():
    print()
    print("                       NA HORA DO SUFOCO!")
    print()
    print()
    print("Parecia uma boa idéia: saiu One Punch Man e Game of Thrones! EU PRECISO ASSISTIR! Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    print("=======================")
    print()
    
            
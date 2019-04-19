def carregar_cenarios():
    cenarios = {
        "inicio": {
            "título": "Saguao do perigo",
            "descrição": "Voce esta no saguao de entrada do insper",
            "opcoes": {"rua em frente ao Insper": "Sair do saguão",
                       "andar 0-S1": "Ir ao subsolo 1",
                       "andar 0-0": "Entrar no Insper"}
        },
        "predio velho": {
            "título": "Saguao do perigo",
            "descrição": "Voce esta no saguao de entrada do insper",
            "opcoes": {"rua em frente ao Insper": "Sair do saguão",
                       "andar 0-S1": "Ir ao subsolo 1",
                       "andar 0-0": "Entrar no Insper"}
        },
        "andar 0-6": {
            "título": "Andar do desespero",
            "descrição": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {"elevador A": "Tomar o elevador para o saguao de entrada",
                       "professor": "Falar com o professor",
                       "insper jr.": "Visitar o Insper Jr. ou o Endeavor",
                       "banheiro": "Ir ao banheiro"}
        },
        "professor": {
            "título": "O monstro do Python",
            "descrição": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "título": "Caverna da tranquilidade",
            "descrição": "Voce esta na biblioteca",
            "opcoes": {"andar 0-0": "Voltar para o saguao de entrada",
                       "fundo": "Avançar para os fundos da biblioteca"}
        },
        "andar 0-S1": {
            'título': 'Abismo, o vazio e a escuridão', 
            'descrição': 'Você está na garagem...', 
            'opcoes': {'elevador A': 'Escolher andar', 
                       'andar 0-S2': 'Ir mais ao fundo', 
                       'laboratorios subsolo': 'Seguir em direção aos laboratórios e ao baja',
                       'predio velho': 'voltar para o terreo',
                       'Uberabinha': 'Seguir a rua para a rua Uberabinha',
                       'bicicletario': 'Entrar no bicicletário',
                       'banheiro': 'Ir ao banheiro'}
        },
        "rua em frente ao Insper": {
            "título": 'Os portões', 
            "descrição": 'Você saiu do Insper, está na rua', 
            'opcoes': {'predio novo': 'Entrar no prédio novo', 
                       'predio velho': 'Entrar no prédio velho', 
                       'Uberabinha': 'Seguir a rua para a rua Uberabinha',
                       'saboroso': 'Ir para o Saboroso'}
        },
        'saboroso': {
            'título': 'El flavors', 
            'descrição': 'Você está no restaurante da esquina', 
            'opcoes': {'comer': 'Gastar R$19.9999999999999999... e recuperar X de HP!', 
                       'beber agua': 'Retornar sua adrenalina em X%! Apenas R$3!', 
                       'conversar com Daniel Guzzo': 'Daniel?',
                       'rua em frente ao Insper': 'sair do Saboroso'}
        },
        'predio novo': {
            'título': 'Fortaleza da Engenharia',
            'descrição': 'O prédio novo do Insper, majoritariamente ocupado por alunos e laboratórios exclusivos da Engenharia',
            'opcoes': {'elevador': 'Escolher andar',
                       'rua na frente do Insper': 'sair do prédio novo'}
        },
        'elevador': {
            'título': 'O elevador do prédio novo',
            'descrição': 'É auto explicativo!',
            'opcoes': {'andar 1-0': 'Andar 0 do prédio novo; nem precisa do elevador',
                       'andar 1-1': 'Andar 1 do prédio novo',
                       'andar 1-2': 'Andar 2 do prédio novo',
                       'andar 1-3': 'Andar 3 do prédio novo',
                       'andar 1-4': 'Andar 4 do prédio novo',
                       'andar 1-5': 'Andar 5 do prédio novo',
                       'andar 1-6': 'Andar 6 do prédio novo'}
        },
        'elevador A': {
            'título': 'A dádiva dos preguiçosos',
            'descrição': 'Elevador que cobre desde o S3 até o oitavo andar do prédio antigo',
            'opcoes': {'andar 0-S3': 'Terceiro subsolo',
                       'andar 0-S2': 'Segundo subsolo',
                       'andar 0-S1': 'Primeiro subsolo',
                       'andar 0-0': 'Térreo',
                       'andar 0-1': 'Primeiro andar',
                       'andar 0-2': 'Segundo andar',
                       'andar 0-3': 'Terceiro andar',
                       'andar 0-4': 'Quarto andar',
                       'andar 0-5': 'Quinto andar',
                       'andar 0-6': 'Sexto andar',
                       'andar 0-7': 'Sétimo andar',
                       'andar 0-8': 'Oitavo andar'}
        },
        'andar 0-S2': {
            'título': 'As profundezas',
            'descrição': 'Segundo subsolo, escuro e vazio',
            'opcoes': {'andar 0-S1': 'subir um andar',
                       'andar 0-S3': 'descer um andar',
                       'elevador A': 'pegar o elevador',
                       'banheiro': 'Ir ao banheiro'}
        },
        'andar 0-S3': {
            'título': 'O fundo',
            'descrição': 'O ponto mais profundo do Insper, vazio e imerso em breu',
            'opcoes': {'andar 0-S2': 'subir um andar',
                       'elevador A': 'Pegar o elevador e sair dali',
                       'banheiro': 'Ir ao banheiro'}
        },
        'andar 0-0': {
            'título': 'O paraíso das possibilidades',
            'descrição': 'Andar térreo do prédio antigo',
            'opcoes': {'elevador A': 'ir para outros andares de elevador',
                       'andar 0-1': 'subir um andar',
                       'andar 0-S1': 'descer um andar',
                       'lanchonete': 'Casa do Pão de Queijo, com cookies, suco e café!',
                       'banheiro': 'Ir ao banheiro',
                       'salas de reunião': 'Salas para fazer reuniões',
                       'antessala': 'Antessala do auditório',
                       'biblioteca': 'Biblioteca Telles',
                       'atendimento ao aluno': 'Balcão de atendimento'}
        },
        'fundo': {
            'título': 'Serenidade',
            'descrição': 'O fundo da biblioteca',
            'opcoes': {'andar 0-0': 'sair da biblioteca',
                       'aquarios biblioteca': 'sentar em um aquário',
                       'poltronas confortáveis': 'Descansar em uma poltrona',
                       'balcao': 'Retirar um livro',
                       'mesas de estudo': 'pegar uma mesa e uma lousa para estudar',
                       'cubiculos': 'Sentar em um cubículo para descansar',
                       'computadores': 'Observar as pessoas mexendo nos computadores da biblioteca'}
        },
        'balcao': {
            'título': 'Balcão de atendimento',
            'descrição': 'O balcão de atendimento da biblioteca',
            'opcoes': {'biblioteca': 'fazer alguma outra coisa',
                       'retirar': 'adicionar um livro ao seu inventário'}
        },
        'aquarios biblioteca': {
            'título': 'Bolhas de reflexão',
            'descrição': 'Os aquários de reunião da biblioteca',
            'opcoes': {'fundo': 'sair do aquário'}
        },
        'poltronas confortáveis': {
            'título': 'Poltronas confortáveis',
            'descrição': 'Poltronas confortáveis... o que você esperava que eu dissesse?',
            'opcoes': {'fundo': 'Chega de descansar, faça alguma coisa'}
        },
        'mesas de estudo': {
            'título': 'Bastião do foco',
            'descrição': 'Mesas e lousas espalhadas de modo a permiti-lo focar intensamente nos estudos',
            'opcoes': {'fundo': 'Estudar é legal, mas temos coisas a fazer'}
        },
        'cubiculos': {
            'título': 'Cubículos',
            'descrição': 'Não tem muito a ser dito... eles são confortáveis e bons para estudar',
            'opcoes': {'fundo': 'Hora de trabalhar um pouco'}
        },
        'computadores': {
            'título': 'O futuro discreto',
            'descrição': 'Você não sabe, mas um dia será você lá',
            'opcoes': {'fundo': 'Ficar parado não vai te levar a lugar nenhum'}
        },
        'lanchonete': {
            'título': 'Casa do Pão de Queijo',
            'descrição': 'Um bom lugar para descansar e recuperar as forças',
            'opcoes': {'comprar': 'comprar alguma coisa',
                       'andar 0-0': 'continuar explorando'}
        },
        'Uberabinha': {
            'título': 'A fronteira do tempo',
            'descrição': 'Rua que separa o prédio novo e o prédio antigo do Insper',
            'opcoes': {'rua em frente ao Insper': 'Ir para a rua Quatá',
                       'andar 0-S1': 'entrar na garagem do Insper'}
        },
        'laboratorios subsolo': {
            'título': 'A gruta do desenvolvimento',
            'descrição': 'No escuro e na solidão, valentes cientistas se instalaram e desenvolvem suas atividades, longe do Insper e de outras pessoas',
            'opcoes': {'andar 0-S1': 'Voltar',
                       'baja': 'Oficina do Baja, o maior centro de desenvolvimento de tecnologia de transporte',
                       'tech lab': 'O Tech Lab do Insper, o laboratório mais bem aparelhado dos dois prédios',
                       'pneumatica': 'Laboratório de Pneumática e Hidráulica',
                       'automacao': 'Laboratório de Automação e Controle'}
        },
        'tech lab': {
            'título': 'O ninho do Paradigma',
            'descrição': 'No meio do estacionamento, o Tech Lab brilha com sua tecnologia de ponta e seus aparelhos exclusivos, oferecendo segurança e esperança',
            'opcoes': {'laboratorios subsolo': 'Sair do Tech Lab',
                       'guru tech': 'Falar com um guru do Tech Lab'}
        },
        'baja': {
            'título': 'Oficina do Baja',
            'descrição': 'O maior centro de desenvolvimento de tecnologia de transportes do Insper',
            'opcoes': {'laboratorios subsolo': 'voltar',
                       'veterano do baja': 'Falar com o veterano que está na oficina'}
        },
        'pneumatica': {
            'título': 'Laboratório de Pneumática e Hidráulica',
            'descrição': 'Algumas mesas e cadeiras, anotações na lousa, mas não tem ninguém',
            'opcoes': {'laboratorios subsolo': 'voltar'}
        },
        'automacao': {
            'título': 'Laboratório de Automação e Controle',
            'descrição': 'Algumas mesas e cadeiras, anotações na lousa, mas não tem ninguém',
            'opcoes': {'laboratorios subsolo': 'voltar'}
        },
        'antessala': {
            'título': 'O santuário da música',
            'descrição': 'Sala ampla que fica no meio do caminho entre a entrada e o auditório',
            'opcoes': {'andar 0-0': 'sair da antessala',
                       'piano': 'Ouvir o piano e relaxar',
                       'auditorio': 'Entrar no Auditório'}
        },
        'piano': {
            'título': 'O piano',
            'descrição': 'Piano localizado na antessala, seu som é muito bonito. Alguém está tocando o piano',
            'opcoes': {'antessala': 'Continuar explorando'}
        },
        'auditorio': {
            'título': 'Auditório',
            'descrição': 'É o auditório do Insper, com suas poltronas confortáveis',
            'opcoes': {'antessala': 'voltar'}
        },
        'banheiro': {
            'título': 'Castelo do alívio',
            'descrição': 'É um banheiro comum. Você faz suas necessidades, dá a descarga, lava as mãos e sai',
            'opcoes': {'andar 0-0': 'térreo do prédio antigo',
                       'andar 0-1': 'primeiro andar do prédio antigo',
                       'andar 0-2': 'segundo andar do prédio antigo',
                       'andar 0-3': 'terceiro andar do prédio antigo',
                       'andar 0-4': 'quarto andar do prédio antigo',
                       'andar 0-5': 'quinto andar do prédio antigo',
                       'andar 0-6': 'sexto andar do prédio antigo',
                       'andar 1-0': 'térreo do prédio novo',
                       'andar 1-1': 'primeiro andar do prédio novo',
                       'andar 1-2': 'segundo andar do prédio novo',
                       'andar 1-3': 'terceiro andar do prédio novo',
                       'andar 1-4': 'quarto andar do prédio novo',
                       'andar 1-5': 'quinto andar do prédio novo',
                       'andar 1-6': 'sexto andar do prédio novo',
                       'andar 0-S1': 'primeiro subsolo do prédio antigo',
                       'andar 0-S2': 'segundo subsolo do prédio antigo',
                       'andar 0-S3': 'terceiro subsolo do prédio antigo'}
        },
        'insper jr.': {
            'título': 'Gente séria',
            'descrição': 'O Insper Jr. e o Endeavor são empresas de verdade no Insper, e, como eles são muito sérios sobre o trabalho deles, você pode apenas vê-los trabalhando',
            'opcoes': {'andar 0-6': 'voltar'}
        }
    }

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inicio(cenario_atual):
    print(cenario_atual["título"])
    print(cenario_atual["descrição"])

def situacao():
    with open("NA HORA DO SUFOCO.txt", "r",encoding="utf8") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
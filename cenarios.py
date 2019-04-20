﻿def carregar_cenarios():
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
                "inimigos" : ["Ayres", "Elemental"]
            "título": "O monstro do Python",
            "descrição": "Voce foi pedir para o professor adiar o EP. O professor revelou que é um monstro disfarçado e devorou sua alma.",
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
            'título': 'Flavoroso', 
            'descrição': 'Você está no restaurante da esquina', 
            'opcoes': {'comer': 'Gastar R$19.9999999999999999... e recuperar X de HP!', 
                       'beber agua': 'Retornar sua adrenalina em X%! Apenas R$3!', 
                       'conversar com Daniel Guzzo': 'Daniel?',
                       'rua em frente ao Insper': 'sair do Saboroso'}
        },
        'predio novo': {
            'título': 'Fortaleza da Engenharia',
            'descrição': 'O prédio novo do Insper, majoritariamente ocupado por alunos e laboratórios exclusivos da Engenharia',
            'opcoes': {'andar 1-0': 'entrar no prédio novo',
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
                       'andar 0-6': 'Sexto andar'}
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
        },
        'andar 1-0': {
            'título': 'Novo térreo',
            'descrição': 'Espaço amplo, tem alguns alunos estudando',
            'opcoes': {'elevador': 'Escolher andar',
                       'andar 1-1': 'Subir as escadas',
                       'area de estudo': 'sentar e estudar um pouco, como os outros alunos',
                       'rua em frente ao Insper': 'sair do prédio novo',
                       'banheiro': 'Ir ao banheiro',
                       'novo subsolo': 'Descer um andar',
                       'cemp': 'Centro de Empreendedorismo do prédio novo'}
        },
        'novo subsolo': {
            'título': 'Acesso restrito',
            'descrição': 'Não é permitido acessar o subsolo do prédio novo',
            'opcoes': {'andar 1-0': 'desistir e explorar o resto'}
        },
        'cemp': {
            'título': 'Centro de Empreendedorismo do prédio novo',
            'descrição': 'Pessoas sérias fazendo trabalho sério',
            'opcoes': {'andar 1-0': 'continuar explorando'}
        },
        'area de estudo': {
            'título': 'Área de estudo',
            'descrição': 'Ao seu redor, os alunos estão estudando, compenetrados',
            'opcoes': {'andar 1-0': 'Levantar e continuar'}
        },
        'andar 1-1': {
            'título': 'Primeiro andar do prédio novo',
            'descrição': 'Tem um corredor à direita, outro à esquerda e um de aquários',
            'opcoes': {'elevador': 'escolher o andar',
                       'andar 1-2': 'subir as escadas',
                       'andar 1-0': 'descer as escadas',
                       'corredor esquerdo 1-1': 'Ir para a esquerda',
                       'corredor direito 1-1': 'Ir para a direita',
                       'corredor aquarios 1-1': 'Aquários',
                       'banheiro': 'Ir ao banheiro'}
        },
        'andar 1-2': {
            'título': 'Segundo andar do prédio novo',
            'descrição': 'Tem um tobogã, um corredor à direita, outro à esquerda e um de aquários',
            'opcoes': {'elevador': 'escolher o andar',
                       'andar 1-3': 'subir as escadas',
                       'andar 1-1': 'descer as escadas',
                       'andar 1-0': 'descer o tobogã',
                       'corredor esquerdo 1-2': 'Ir para a esquerda',
                       'corredor direito 1-2': 'Ir para a direita',
                       'corredor aquarios 1-2': 'Aquários',
                       'banheiro': 'Ir ao banheiro'}
        },
        'andar 1-3': {
            'título': 'Terceiro andar do prédio novo',
            'descrição': 'Tem um corredor à direita, outro à esquerda e um de aquários',
            'opcoes': {'elevador': 'escolher o andar',
                       'andar 1-4': 'subir as escadas',
                       'andar 1-2': 'descer as escadas',
                       'corredor esquerdo 1-3': 'Ir para a esquerda',
                       'corredor direito 1-3': 'Ir para a direita',
                       'corredor aquarios 1-3': 'Aquários',
                       'banheiro': 'Ir ao banheiro'}
        },
        'andar 1-4': {
            'título': 'Quarto andar do prédio novo',
            'descrição': 'Tem um corredor à direita, outro à esquerda e uma sala',
            'opcoes': {'elevador': 'escolher o andar',
                       'andar 1-5': 'subir as escadas',
                       'andar 1-3': 'descer as escadas',
                       'corredor esquerdo 1-4': 'Ir para a esquerda',
                       'corredor direito 1-4': 'Ir para a direita',
                       'sala 411': 'Entrar na sala',
                       'máquinas de vendas 1-4': 'comprar alguma coisa',
                       'banheiro': 'Ir ao banheiro'}
        },
        'andar 1-5': {
            'título': 'Quinto andar do prédio novo',
            'descrição': 'Tem um corredor à direita, outro à esquerda e um de aquários',
            'opcoes': {'elevador': 'escolher o andar',
                       'andar 1-6': 'subir as escadas',
                       'andar 1-4': 'descer as escadas',
                       'corredor esquerdo 1-5': 'Ir para a esquerda',
                       'corredor direito 1-5': 'Ir para a direita',
                       'corredor aquarios 1-5': 'Aquários',
                       'banheiro': 'Ir ao banheiro'}
        },
        'andar 1-6': {
            'título': 'Sexto andar do prédio novo',
            'descrição': 'Tem mesas, cubículos, uma varanda, a copa e alguns alunos conversando nos sofás',
            'opcoes': {'elevador': 'escolher andar',
                       'andar 1-5': 'descer as escadas',
                       'copa': 'entrar na copa',
                       'varanda': 'ir para o lado externo',
                       'banheiro': 'Ir ao banheiro'}
        },
        'corredor direito 1-1': {
            'título': 'Corredor da direita',
            'descrição': 'É um corredor com duas salas e uma máquina de vendas',
            'opcoes': {'sala 111': 'Sala 111',
                       'sala 112': 'Sala 112',
                       'maquina de vendas 1-1': 'comprar algo',
                       'andar 1-1': 'voltar'}
        },
        'corredor direito 1-2': {
            'título': 'Corredor da direita',
            'descrição': 'É um corredor com duas salas e uma máquina de vendas',
            'opcoes': {'sala 211': 'Sala 211',
                       'sala 212': 'Sala 212',
                       'maquina de vendas 1-2': 'comprar algo',
                       'andar 1-2': 'voltar'}
        },
        'corredor direito 1-3': {
            'título': 'Corredor da direita',
            'descrição': 'É um corredor com duas salas e uma máquina de vendas',
            'opcoes': {'sala 311': 'Sala 311',
                       'sala 312': 'Sala 312',
                       'maquina de vendas 1-3': 'comprar algo',
                       'andar 1-3': 'voltar'}
        },
        'corredor direito 1-4': {
            'título': 'Corredor da direita',
            'descrição': 'É um corredor com três laboratórios',
            'opcoes': {'arq comp': 'Laboratório de Arquitetura da Computação',
                       'supercomp': 'Laboratório de Redes e Supercomputação',
                       'videogame': 'Laboratório de Realidade Virtual e Jogos Virtuais',
                       'andar 1-4': 'voltar'}
        },
        'corredor direito 1-5': {
            'título': 'Corredor da direita',
            'descrição': 'É um corredor com duas salas e uma máquina de vendas',
            'opcoes': {'sala 511': 'Sala 511',
                       'sala 512': 'Sala 512',
                       'andar 1-5': 'voltar'}
        },
        'corredor esquerdo 1-1': {
            'título': 'Corredor da esquerda',
            'descrição': 'Tem duas salas de aula',
            'opcoes': {'sala 113': 'Sala 113',
                       'sala 114': 'Sala 114',
                       'andar 1-1': 'voltar'}
        },
        'corredor esquerdo 1-2': {
            'título': 'Corredor da esquerda',
            'descrição': 'Tem duas salas de aula',
            'opcoes': {'sala 213': 'Sala 213',
                       'sala 214': 'Sala 214',
                       'andar 1-2': 'voltar'}
        },
        'corredor esquerdo 1-3': {
            'título': 'Corredor da esquerda',
            'descrição': 'Tem o FabLab',
            'opcoes': {'FabLab': 'Entrar no FabLab',
                       'andar 1-3': 'voltar'}
        },
        'corredor esquerdo 1-4': {
            'título': 'Corredor da esquerda',
            'descrição': 'É um corredor com três laboratórios',
            'opcoes': {'agil 1': 'Laboratório Ágil 1',
                       'agil 2': 'Laboratório Ágil 2',
                       'exp usab': 'Sala de Experiências de Usabilidade',
                       'andar 1-4': 'voltar'}
        },
        'corredor esquerdo 1-5': {
            'título': 'Corredor da esquerda',
            'descrição': 'Tem duas salas de aula',
            'opcoes': {'sala 513': 'Sala 513',
                       'sala 514': 'Sala 514',
                       'andar 1-5': 'voltar'}
        },
        'sala 111': {
            'título': 'Sala 111',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-1': 'voltar'}
        },
        'sala 112': {
            'título': 'Sala 112',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-1': 'voltar'}
        },
        'sala 211': {
            'título': 'Sala 211',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-2': 'voltar'}
        },
        'sala 212': {
            'título': 'Sala 212',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-2': 'voltar'}
        },
        'sala 311': {
            'título': 'Sala 311',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-3': 'voltar'}
        },
        'sala 312': {
            'título': 'Sala 312',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-3': 'voltar'}
        },
        'sala 411': {
            'título': 'Sala 411',
            'descrição': 'Sala enorme que tem a largura de um corredor de aquários',
            'opcoes': {'andar 1-4': 'voltar'}
        },
        'sala 511': {
            'título': 'Sala 511',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-5': 'voltar'}
        },
        'sala 512': {
            'título': 'Sala 512',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-5': 'voltar'}
        },
        'sala 113': {
            'título': 'Sala 113',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-1': 'voltar'}
        },
        'sala 114': {
            'título': 'Sala 114',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-1': 'voltar'}
        },
        'sala 213': {
            'título': 'Sala 213',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-2': 'voltar'}
        },
        'sala 214': {
            'título': 'Sala 214',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-2': 'voltar'}
        },
        'sala 513': {
            'título': 'Sala 513',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-5': 'voltar'}
        },
        'sala 514': {
            'título': 'Sala 514',
            'descrição': '9 mesas, 6 lousas e algumas canetas',
            'opcoes': {'corredor direito 1-5': 'voltar'}
        },
        'varanda': {
            'título': 'Mirante',
            'descrição': 'Parte ao ar livre do sexto andar do prédio novo, é possível ver boa parte da Faria Lima e da Hélio Pellegrino',
            'opcoes': {'andar 1-6': 'voltar'}
        },
        'copa': {
            'título': 'Rango',
            'descrição': 'Tem um microondas e uma geladeira',
            'opcoes': {'andar 1-6': 'sair da copa'}
        },
        'agil 1': {
            'título': 'Laboratório Ágil 1',
            'descrição': 'A porta requere senha para abrir',
            'opcoes': {'andar 1-4': 'desistir e continuar explorando'}
        },
        'agil 2': {
            'título': 'Laboratório Ágil 2',
            'descrição': 'A porta requere senha para abrir',
            'opcoes': {'andar 1-4': 'desistir e continuar explorando'}
        },
        'exp usab': {
            'título': 'Sala de Experiências de Usabilidade',
            'descrição': 'A porta requere senha para abrir',
            'opcoes': {'andar 1-4': 'desistir e continuar explorando'}
        },
        'arq comp': {
            'título': 'Laboratório de Arquitetura da Computação',
            'descrição': 'A porta requere senha para abrir',
            'opcoes': {'andar 1-4': 'desistir e continuar explorando'}
        },
        'supercomp': {
            'título': 'Laboratório de Redes e Supercomputação',
            'descrição': 'A porta requere senha para abrir',
            'opcoes': {'andar 1-4': 'desistir e continuar explorando'}
        },
        'videogame': {
            'título': 'Laboratório de Realidade Virtual e Jogos Digitais',
            'descrição': 'A porta requere senha para abrir',
            'opcoes': {'andar 1-4': 'desistir e continuar explorando'}
        },
        'FabLab': {
            'título': 'O laboratório',
            'descrição': 'Tem todas as máquinas do FabLab... o guru está mexendo no computador',
            'opcoes': {'andar 1-3': 'sair do FabLab',
                       'guru FabLab': 'Falar com o guru'}
        },
        'corredor aquarios 1-1': {
            'título': 'Bolhas de concentração',
            'descrição': 'Tem 9 aquários, alguns ocupados',
            'opcoes': {'aquario 1-1': 'Pegar um aquario livre',
                       'andar 1-1': 'voltar'}
        },
        'aquario 1-1': {
            'título': 'Aquário',
            'descrição': 'Uma sala aconchegante com uma boa vista e uma atmosfera de foco e concentração',
            'opcoes': {'corredor aquarios 1-1': 'sair do aquário'}
        },
        'corredor aquarios 1-2': {
            'título': 'Bolhas de concentração',
            'descrição': 'Tem 7 aquários, alguns ocupados',
            'opcoes': {'aquario 1-2': 'Pegar um aquario livre',
                       'andar 1-2': 'voltar'}
        },
        'aquario 1-2': {
            'título': 'Aquário',
            'descrição': 'Uma sala aconchegante com uma boa vista e uma atmosfera de foco e concentração',
            'opcoes': {'corredor aquarios 1-2': 'sair do aquário'}
        },
        'corredor aquarios 1-3': {
            'título': 'Bolhas de concentração',
            'descrição': 'Tem 3 aquários, alguns ocupados, e o HelpDesk',
            'opcoes': {'aquario 1-3': 'Pegar um aquario livre',
                       'HelpDesk': ' Falar com alguém do HelpDesk',
                       'andar 1-3': 'voltar'}
        },
        'aquario 1-3': {
            'título': 'Aquário',
            'descrição': 'Uma sala aconchegante com uma boa vista e uma atmosfera de foco e concentração',
            'opcoes': {'corredor aquarios 1-3': 'sair do aquário'}
        },
        'corredor aquarios 1-5': {
            'título': 'Bolhas de concentração',
            'descrição': 'Tem 7 aquários, alguns ocupados',
            'opcoes': {'aquario 1-5': 'Pegar um aquario livre',
                       'andar 1-5': 'voltar'}
        },
        'aquario 1-5': {
            'título': 'Aquário',
            'descrição': 'Uma sala aconchegante com uma boa vista e uma atmosfera de foco e concentração',
            'opcoes': {'corredor aquarios 1-5': 'sair do aquário'}
        },
        'andar 0-1': {
            'título': 'Primeiro andar do prédio antigo',
            'descrição': 'Corredor amplo',
            'opcoes': {'andar 0-2': 'Subir as escadas',
                       'andar 0-0': 'Descer as escadas',
                       'elevador A': 'escolher andar',
                       'banheiro': 'Ir no banheiro',
                       'sala amador aguiar': 'Sala Amador Aguiar',
                       'sala sebastiao camargo': 'Sala Sebastião Camargo',
                       'sala walther moreira sales': 'Sala Walther Moreira Sales',
                       'sala jose ermirio de moraes': 'Sala José Ermírio de Moraes Filho',
                       'sala olavo setubal': 'Sala Olavo Setubal',
                       'sala jorge paulo lemann': 'Sala Jorge Paulo Lemann',
                       'maquina de vendas 0-1': 'Máquina de vendas',
                       'estudo individual': 'Área de estudo individual'}
        },
        'andar 0-2': {
            'título': 'Segundo andar do prédio antigo',
            'descrição': 'Corredor amplo',
            'opcoes': {'andar 0-3': 'Subir as escadas',
                       'andar 0-1': 'Descer as escadas',
                       'elevador A': 'escolher andar',
                       'banheiro': 'Ir no banheiro',
                       'sala luiz martins de souza dantas': 'Sala Luiz Martins de Souza Dantas',
                       'sala paulo renato souza': 'Sala Paulo Renato Souza',
                       'sala marcos lopes': 'Sala Marcos Lopes',
                       'sala 205': 'Sala 205',
                       'sala 206': 'Sala 206',
                       'sala graber': 'Sala Graber',
                       'sala alberto bandeira de queiroz': 'Sala Alberto Bandeira de Queiroz',
                       'sala 204': 'Sala 204',
                       'helpdesk': 'HelpDesk do prédio antigo',
                       'sala 203': 'Sala 203',
                       'sala octavio gouvea de bulhoes': 'Sala Octavia Gouvea de Bulhões',
                       'sala ottolara resende': 'Sala Ottolara Resende',
                       'sala peter drucker': 'Sala Peter Drucker',
                       'sala mario haberfeld': 'Sala Mario Haberfeld',
                       'sala 201': 'Sala 201',
                       'sala 202': 'Sala 202',
                       'maquina de vendas 0-1': 'Máquina de vendas',
                       'balcao de impressao': 'Balcão de Impressão',
                       'estudo grupal 0-2-1': 'Sala de Estudo em grupo 01',
                       'armarios 0-2': 'Armários'}
        },
        'andar 0-3': {
            'título': 'Terceiro andar do prédio antigo',
            'descrição': 'Corredor amplo',
            'opcoes': {'andar 0-4': 'Subir as escadas',
                       'andar 0-2': 'Descer as escadas',
                       'elevador A': 'escolher andar',
                       'banheiro': 'Ir no banheiro',
                       'armarios 0-3': 'Armários',
                       'sala bovespa 1': 'Sala BM&F Bovespa 1',
                       'sala bovespa 2': 'Sala BM&F Bovespa 2',
                       'sala vicente falconi campos': 'Sala Vicente Falconi Campos',
                       'sala joao gerdau': 'Sala João Gerdau',
                       'sala victor civita': 'Sala Victor Civita',
                       'sala max feffer': 'Sala Max Feffer',
                       'sala roberto cochrane simonsen': 'Sala Roberto Cochrane Simonsen',
                       'maquina de vendas 0-3': 'Máquina de vendas',
                       'estudo grupal 0-3-1': 'Sala de Estudo em grupo 01',
                       'estudo grupal 0-3-2': 'Sala de Estudo em grupo 02',
                       'area de lazer 0-3': 'Área de lazer',
                       'sala eugenio gudin': 'Sala Eugênio Gudin',
                       'sala eudoro villela': 'Sala Eudoro Villela',
                       'sala francisca': 'Sala Francisca JPA Moraes',
                       'sala 308': 'Sala 308'}
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
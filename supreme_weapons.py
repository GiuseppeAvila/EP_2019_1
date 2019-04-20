def TP(cenarios_conhecidos):
    local_desejado = input("Escolha um local que deseja derivar: ")
    escolhendo = True
    while escolhendo:
        if local_desejado in cenarios_conhecidos:
            return local_desejado
            escolhendo = False
        else:
            print("Você não conhece esse local, não faço mágica, isso é matemática!")
            local_desejado = input("Escolha um local que deseja derivar: ")

def DIM(dano_fisico,defesa):
    multiplicador = 0
    buff = 0
    dano_fisico *= multiplicador
    defesa += buff
    return [dano_fisico,defesa]

def SCOT(dano_magico):
    dano_adicional = 0
    dano_magico += dano_adicional
    return dano_magico


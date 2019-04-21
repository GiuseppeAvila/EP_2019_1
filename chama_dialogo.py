# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:22:31 2019

@author: Erick
"""

def dialogo(dialogos,nome):
    import random
    for chave in dialogos.keys():
        if chave == nome:
            indice = random.randint(0,len(dialogos[nome])-1)
            texto = dialogo[nome][indice]
    return texto

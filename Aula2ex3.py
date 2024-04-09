#Codigo com uma busca binaria

import random

def gerador_de_lista_com_elementos_inteiros(quantidade, maximo):
    return (random.sample(range(-1, maximo + 1), quantidade))

def busca_binaria(lista, elemento):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None

quantidade = 10
maximo = 50
lista_gerada = gerador_de_lista_com_elementos_inteiros(quantidade, maximo)
print(lista_gerada)

elemento = 42
posicao = busca_binaria(lista_gerada, elemento)
print(f"Posição de {elemento} na lista: {posicao}")

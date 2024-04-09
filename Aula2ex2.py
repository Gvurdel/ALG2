#Você deverá implementar um algoritmo que execute a mesma função do método index() 
# já implementado na estrutura de dados lista do python.
#minha_lista.index(elemento)

#Crie uma função que receba como parâmetros uma lista e a informação a ser encontrada
#nesta lista.
#Esta função deverá retornar a posição da lista onde a informação foi encontrada,
#ou retornar None, caso a informação não seja encontrada.

import random

def gerador_de_lista_com_elementos_inteiros(quantidade, maximo):
    return random.sample(range(-1, maximo + 1), quantidade)

def minha_index(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return None

quantidade = 10
maximo = 50
lista_gerada = gerador_de_lista_com_elementos_inteiros(quantidade, maximo)
print(lista_gerada)

elemento = 42
posicao = minha_index(lista_gerada, elemento)
print(f"Posição de {elemento} na lista: {posicao}")


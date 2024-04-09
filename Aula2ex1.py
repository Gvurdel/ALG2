
#Crie uma função que receba como parâmetro a quantidade de elementos e o valor máximo a ser gerado e retorne uma lista com esses elementos.
#Exemplo: gerador_de_lista_com_elementos_inteiros(10, 50), onde:

#10 -> quantidade de elementos na lista
#50 -> elementos entre -1 e 50.

import random

def gerador_de_lista_com_elementos_inteiros(quantidade, maximo):
    return [random.randint(-1, maximo) for _ in range(quantidade)]

quantidade = 10
maximo = 50
lista_gerada = gerador_de_lista_com_elementos_inteiros(quantidade, maximo)
print(lista_gerada)


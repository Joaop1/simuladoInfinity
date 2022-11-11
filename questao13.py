'''Pedir 10 números, se o número for par, vai para uma lista,
se for impar, vai para outra lista. Ao final, mostrar as duas listas,
a soma dos pares, a soma dos impares e a soma das duas listas'''
from typing import List, Any

listapar = []
listaimpar = []

for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
print(listapar)
print(listaimpar)
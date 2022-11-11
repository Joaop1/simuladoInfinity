'''Solicite a idade de 5 pessoas e ao final conte quantas pessoas
são maiores de idade, a soma de todas as idades, a média das idades,
o valor máximo, o valor mínimo, ordene de forma crescente e decrescente.'''
lista = []
maior = []
for i in range(5):
    idade = int(input(f'Digite a {i +1}ª idade: '))
    lista.append(idade)
    if idade >= 18:
        maior.append(idade)
maior_idade = len(maior)
print(f'Temos {maior_idade} maior(es) de idade')
soma = sum(lista)
print(f'A soma das idades é {soma}')
media = sum(lista) / len(lista)
print(f'A média das idades é {media}')
maximo = max(lista)
print(f'A maior idade informada é {maximo}')
minimo = min(lista)
print(f'A menor idade informada é {minimo}')
crescente = sorted(lista)
print(f'Ordem crescente: {crescente}')
decrescente = sorted(lista, reverse=True)
print(f'Ordem decrescente: {decrescente}')

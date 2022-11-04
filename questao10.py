'''Peça 5 números e informe a soma e o maior número (OBS: sem utilizar listas)'''
soma = 0

for i in range(5):
    numero = int(input(f'Informe o {i + 1}º número: '))
    soma += numero

print(soma)


'''Crie um algoritmo que indique se um número é positivo ou negativo'''
numero = int(input('Digite um número inteiro: '))
if numero < 0:
    print(f'O número {numero} é negativo!')
elif numero > 0:
    print(f'O numero {numero} é positivo!')
else:
    print('Você digitou o número zero!')

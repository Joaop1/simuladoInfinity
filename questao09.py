'''Crie um algoritmo que indique se um número é par ou impar'''

numero = int(input('Informe um número positivo: '))
if numero == 0:
    print('Você digitou o número zero!')
elif numero % 2 == 1:
    print(f'O número {numero} é impar!')
else:
    print(f'O número {numero} é par!')


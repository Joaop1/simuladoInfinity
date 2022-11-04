'''Faça um programa que pergunta a temperatura em graus Celsius e responde a temperatura correspondente em
graus Fahrenheit.'''

temp = float(input('Informe a temperatura em graus celsius: '))
conv = temp * 1.8 + 32
print(f'Convertendo para fahrenheit seria {conv}ºf')
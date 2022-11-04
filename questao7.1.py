'''Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a
temperatura correspondente em graus Celsius.'''

temp = float(input('Informe a temperatura em graus fahrenheit: '))
conv = (temp - 32) / 1.8
print(f'Convertendo para celsius seria {conv}ºc')
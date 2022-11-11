'''Programa para cálculo de IMC e ao final informar em qual categoria
o usuário se encontra.'''
peso = float(input('Digite o seu peso atual: '))
alt = float(input('Digite sua altura: '))

imc = peso / (alt * alt)
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc >= 18.5 and imc <= 24.9:
    print('Parabêns, você está com o peso normal!')
elif imc >= 25 and imc <= 29.9:
    print('Você está com excesso de peso!')
elif imc >= 30 and imc <= 34.9:
    print('Você está com obesidade classe I')
elif imc >= 35 and imc <= 39.9:
    print('Vocẽ está com obesidade classe II')
else:
    print('Vocẽ está com obesidade classe III')
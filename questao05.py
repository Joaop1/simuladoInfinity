#Crie um algoritmo que informe o tipo de um valor informado pelo usuário

valor = input('Digite um valor: ')
tipo = input('Informe o tipo desse valor: \n[1] Número inteiro\n[2] Número decimal\n[3] Texto\n[4] Lógico(True/False]\n')
if tipo == '1':
    valor = int(valor)
    print(type(valor))
elif tipo == '2':
    valor = float(valor)
    print(type(valor))
elif tipo == '3':
    valor = str(valor)
    print(type(valor))
elif tipo == '4':
    valor = bool(valor)
    print(type(valor))
else:
    print('Por favor, volte e escolha o tipo do valor digitado!')
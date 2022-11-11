'''Crie uma tupla com a latitude e longitude de uma cidade e depois
imprima em tela. Edite a tupla anterior com os valores de outra cidade e
imprima novamente.'''

latiLongi = (-3.731862, -38.526669)
print(f'A latitude de Fortaleza é {latiLongi[0]} e a longitude é {latiLongi[1]}')

lista1 = list(latiLongi)

del latiLongi
print(lista1)


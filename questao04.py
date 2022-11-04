#Faça um programa que solicite a nota das 4 provas de um aluno e responde a sua média.
notas = 0
for i in range(4):
    nota = int(input(f'Informe a sua {i + 1}ª nota: '))
    notas = notas + nota
media = notas / 4
print(media)
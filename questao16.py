'''Criar um dicionário com as informações de uma única pessoa.
Nome, Endereço, Data de nascimento, CPF, Nacionalidade'''

pessoa = {}
pessoa['nome'] = input('Digite seu nome: ')
pessoa['endereco'] = input('Digite o seu endereço: ')
pessoa['nascimento'] = input('Digite sua data de nascimento: ')
pessoa['cpf'] = input('Digite seu CPF: ')
pessoa['nacionalidade'] = input('Digite a sua nascionalidade:')
print(pessoa)

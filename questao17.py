#Imprimir os itens, as chaves e os valores do dicionário anterior
pessoa = {}
pessoa['nome'] = input('Digite seu nome: ')
pessoa['endereco'] = input('Digite o seu endereço: ')
pessoa['nascimento'] = input('Digite sua data de nascimento: ')
pessoa['cpf'] = input('Digite seu CPF: ')
pessoa['nacionalidade'] = input('Digite a sua nascionalidade:')
print(pessoa)
print(pessoa.items())
print(pessoa.keys())
print(pessoa.values())
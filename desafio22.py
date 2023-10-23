nome = str(input('Qual o seu nome completo? '))
print("""Seu nome em maiúsculas: {}
Seu nome em minúsculas: {}
Seu nome tem ao todo {} letras""" .format(nome.upper(), nome.lower(), len(nome) - nome.count(' ')))
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele possui {len(nome[0])} letras.')

"""Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas,
o nome com todas as letras minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras
possuem o primeiro nome."""

nome = str(input('Qual o seu nome completo? '))
print("""Seu nome em maiúsculas: {}
Seu nome em minúsculas: {}
Seu nome tem ao todo {} letras""" .format(nome.upper(), nome.lower(), len(nome) - nome.count(' ')))
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele possui {len(nome[0])} letras.')

#também é possível encontrar o primeiro nome procurando o primeiro espaço usando nome.find(' ')

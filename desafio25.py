'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = str(input('Qual o seu nome completo? '))
nome = nome.strip().lower().split()
if 'silva' in nome:
    print('É um silva!')
else:
    print('Não é um silva!')

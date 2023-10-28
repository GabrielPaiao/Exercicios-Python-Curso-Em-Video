'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint

n = randint(0, 5)
r = int(input('Pensei em um numero entre em 0 e 5, consegue adivinhar qual? '))
if n == r:
    print('Parabens, voce acertou!')
else:
    print(f'Nao foi dessa vez :c\nA resposta era {n}!')

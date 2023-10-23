"""Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada"""

n = int(input('Insira um numero para que eu mostre sua tabuada: '))
for cont in range(11):
    print('{} x {} = {}' .format(n, cont, n*cont))

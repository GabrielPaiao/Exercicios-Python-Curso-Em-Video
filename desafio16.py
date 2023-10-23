"""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira"""

n = float(input('Insira um numero fracionado: '))
print('{:.0f}'.format(n))

#CÓDIGO ALTERNATIVO:
#from math import trunc
#print(trunc(n))
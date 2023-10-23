"""Escreva um programa que converta uma temperatura digitada em Celsius para Fahrenheit"""

c = float(input('Insira uma temperatura em CELSIUS: '))
print('Essa temperatura, convertida para FAHRENHEIT, é aproximadamente: F{:.2f}!'.format(c * 9/5 + 32))

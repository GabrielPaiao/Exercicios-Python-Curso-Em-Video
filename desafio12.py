"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto"""

preco = float(input('Qual o preço do produto? '))
print('Com 5% de desconto, esse mesmo produto passará a custar R${:.2f}!' .format(preco-preco*5/100))

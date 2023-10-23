"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
pode comprar.
Considere U$1,00 = R$3,27"""

real = float(input('Quanto você tem? R$'))
print('Com esse valor, você pode comprar U${:.2f}!'.format(real / 3.27))

"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2"""

larg = float(input('Qual a largura da parede(m)? '))
h = float(input('Qual a altura da parede(m)? '))
print('A área da parede equivale a {:.2f}.\n'
      'Serão necessários {:.2f}l de tinta para pintá-la.' .format(larg*h, larg*h / 2))

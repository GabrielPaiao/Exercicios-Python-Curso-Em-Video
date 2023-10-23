'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, radians

ang = float(input('Insira a medida do angulo: '))
print('Seno: {:.2}\n'
      'Cosseno: {:.2}\n'
      'Tangente: {:.2}'.format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
#precisa de conversão com a função .radians pq as funções de math nao retornamo valor em graus centigrados

'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um
triângulo'''

retas = []

for cont in range(3):
    retas.append(float(input(f'Insira o valor da {cont + 1}a reta: ')))

if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('Essas medidas podem formar um triângulo!')
else:
    print('Essas medidas não podem formar um triângulo :c')

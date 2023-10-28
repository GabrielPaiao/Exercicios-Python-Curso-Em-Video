'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

numeros = []

for cont in range(3):
    numeros.append(int(input('Insira um numero: ')))

numeros.sort()
print(f'O maior numero digitado foi: {numeros[-1]}!\nE o menor foi: {numeros[0]}!')

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = -1
while (n < 0 or n > 9999):
    n = int(input('Insira um numero entre 1 - 9999: '))
    if (n < 0 or n > 9999):
        print('Valor invalido.\n')

unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print(f"""Milhar: {milhar}
Centena: {centena}
Dezena: {dezena}
Unidade: {unidade}""")

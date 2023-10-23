"""Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade
de dias pelos quais o mesmo fora alugado. Calcule o preço a se pagat sabendo que o carro custa R$60,00
por dia e R$0,15 por KM rodado."""

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
print('O preço a pagar é de R${}!'.format(dias * 60 + km * 0.15))

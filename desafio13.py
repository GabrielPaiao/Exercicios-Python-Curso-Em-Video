"""Faça um programa que leia o sakário de um funcionário e mostre seu novo salário, com 15% de aumento."""

sal = float(input('Insira o seu salario: R$'))
print('Após um reajuste de 15%, seu novo salário é de R${:.2f}!\nParabéns!' .format(sal + sal*15/100))

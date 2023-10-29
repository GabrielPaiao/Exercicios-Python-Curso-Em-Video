'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Insira o salário de um funcionário: R$'))

if sal > 1250:
    print(f'O salário sofreu um reajuste de 10%: R${sal + (sal * 0,1)}')
else:
    print(f'O salário sofreu um reajuste de 1%%: R${sal + (sal * 0,15)}')

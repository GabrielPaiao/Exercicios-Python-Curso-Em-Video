'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
dos alunos e escrevendo na tela o nome do escolhido.
'''
from random import choice

alunos = []
for cont in range(5):
    alunos.append(input('{}o aluno: '.format(cont+1)))
print('O aluno sorteado(a) foi: {}!'.format(choice(alunos)))

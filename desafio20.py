"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle

alunos = []
for cont in range(5):
    alunos.append(input('ALUNO {}: '.format(cont + 1)))
shuffle(alunos)
print('A ordem decidida para a apresentação foi:\n{}'.format(alunos))

from random import shuffle

alunos = []
for cont in range(5):
    alunos.append(input('ALUNO {}: '.format(cont + 1)))
shuffle(alunos)
print('A ordem decidida para a apresentação foi:\n{}'.format(alunos))

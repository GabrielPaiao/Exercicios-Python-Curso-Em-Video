'''29. Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima
do limite.'''

vel = float(input('Velocidade: '))
if vel > 80:
    print('Voce deve pagar uma multa no valor de R${:.2f}!'.format(7 * (vel - 80)))
else:
    print('Está dentro do limite.')

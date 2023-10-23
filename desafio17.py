import math

c1 = float(input('Qual a dimensão do cateto oposto: '))
c2 = float(input('E a do cateto adjacente?: '))
print('O comprimento da hiotenusa é: {:.2f}'.format(math.hypot(c1, c2)))
#hipotenusa = math.sqrt((pow(c1, 2) + pow(c2, 2))

larg = float(input('Qual a largura da parede(m)? '))
h = float(input('Qual a altura da parede(m)? '))
print('A área da parede equivale a {:.2f}.\n'
      'Serão necessários {:.2f}l de tinta para pintá-la.' .format(larg*h, larg*h / 2))

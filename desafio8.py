metros = float(input('Insira uma medida em METROS: '))
print('Essa medida em:\n'
      'Centímetros: {:.3}\n'
      'Milímetros: {:.3}' .format(metros*100, metros*1000))
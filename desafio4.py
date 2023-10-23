"""Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações
possíveis sobre ele."""

msg = input('Insira sua mensagem: ')

print("""Tipo primitivo: {}
Tem espaçamento? {}
É um número? {}
É uma letra? {}
É uma exp. alfanumérica? {}
É capitalizada? {}""".format(type(msg), msg.isspace(), msg.isnumeric(), msg.isalpha(), msg.isalnum(), msg.istitle()))
if msg.isalpha():
    print('É maiúscula? {}' .format(msg.isupper()))
    print('É minúscula? {}' .format(msg.islower()))

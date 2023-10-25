'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”'''

cidade = str(input('Cidade: '))
cidade = cidade.lower().strip().split()
#nao precisa necessariamente do split, 'santa' tem 5 letras, entao da pra verificar se cidade[0:5] = 'santo'
if (cidade[0] == 'santo' or cidade[0] == 'santa'):
    print('Sua cidade começa com "Santo" no nome!')
else:
    print('Sua cidade nao começa com "Santo" no nome!')
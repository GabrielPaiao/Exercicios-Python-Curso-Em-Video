'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: '))
print(f"A letra 'A' aparece {frase.strip().lower().count('a')}x na frase.\n"
      f"Sendo a primeira vez na posição {frase.strip().lower().find('a')}\n"
      f"E a última na posição {frase.strip().lower().rfind('a')}!")

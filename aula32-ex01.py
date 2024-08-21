"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_inteiro = input('Informe um número inteiro: ')

if num_inteiro.isdigit():
    num_inteiro = int(num_inteiro)
    if num_inteiro % 2 == 0:
        print(f'O número "{num_inteiro}" é um número par.')
    elif num_inteiro % 2 == 1:
        print(f'O número "{num_inteiro}" é um número ímpar.')
else:
    print(f'O número {num_inteiro} não é um número inteiro.')
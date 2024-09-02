# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicaçao = multiplicar(1, 2, 3, 4, 5)
print(multiplicaçao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(n):
    num = ""
    if n % 2 == 0:
        num = "O número é par"
    else:
        num = "O número é ímpar"
    return num

args = par_impar(3)
print(args)


"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print(a, b, c):
#     print('Várias')
#     print('Várias')
#     print('Várias')
#     print('Várias')

# def imprimir(a, b, c):
#     print(a, b, c)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu noem é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

prim_nome = input('Informe seu primeiro nome: ')
tm_nome = len(prim_nome)

if tm_nome > 2:
    if tm_nome <= 4:
        print("Seu nome é curto")
    elif 5 <= len(prim_nome) <= 6:
        print("Seu nome é normal")
    elif len(prim_nome) > 6:
        print("Seu nome é muito grande")
else:
    print('Digite ao menos 3 letras.')

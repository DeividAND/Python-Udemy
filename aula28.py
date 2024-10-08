"""
Exercício
Peça ao usuário para digitar seu nome 
peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = (input('Informe seu nome: ')).strip()
idade = (input('Informe sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém "espaço(s)."')
    else:
        print('Seu nome não contém "espaços".')
    print(f'Seu nome contém {len(nome)} caracteres digitados.')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[-1]}"')
else:
    print('Desculpe, você deixou campos vazios.')
    



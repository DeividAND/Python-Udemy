"""
Iterando strings com while
"""
#       01234567891011121314
nome = 'Deivid augusto'  # Iteráveis
#      1413121110987654321
tamanho_nome = len(nome)

indice = 0
novo_nome =''
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
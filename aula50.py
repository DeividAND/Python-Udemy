"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']

indices_lista = range(len(lista))

for indice in indices_lista:
    print(indice, lista[indice], type(lista[indice]))
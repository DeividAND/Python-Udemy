"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hecadecimal (ABCDEF0123456789)
"""
nome = 'Augusto'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))
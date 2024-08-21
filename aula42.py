frase = 'O Python é uma linguegem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais = 0
maior_qtd = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtdl_apareceu_atual = frase.count(letra_atual)

    if apareceu_mais < qtdl_apareceu_atual:
        apareceu_mais = qtdl_apareceu_atual
        maior_qtd = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{maior_qtd}" que apareceu '
    f'{apareceu_mais}x'
)
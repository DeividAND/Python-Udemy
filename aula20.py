primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'o {primeiro_valor} é maior')
    print(f'o {segundo_valor} é menor')
elif segundo_valor > primeiro_valor:
    print(f'o {segundo_valor} é maior')
    print(f'o {primeiro_valor} é menor')
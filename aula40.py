""" Calculadora com while """

while True:
    n1 = float(input('Informe o primeiro número: '))
    n2 = float(input('Informe o segundo número: '))
    print('*ESCOLHA UMA OPÇÃO*\
          1.SOMA\
          2.SUNTRAÇÃO\
          3.MULTIPLICAÇÃO\
          4.DIVISÃO')
    op = int(input('Informe a operação que deseja realizar: 1/2/3/4: '))
    while not 1 <= op <= 4:
        op = int(input('Informe a operação que deseja realizar: 1/2/3/4: '))
        print('Por favor informar opções válidas.')
        if 1 <= op <= 4:
            break
    if op == 1:
        soma = n1 +  n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif op == 2:
        sub = n1 - n2
        print(f'A subtração entre {n1} - {n2} = {sub}')
    elif op == 3:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} = {mult}')
    elif op == 4:
        div = n1 / n2
        print(f'A subtração entre {n1} / {n2} = {div}')

    op2 = str(input('Deseja continuar ? [S][N] ')).upper().strip()
    while op2 != 'S' and op2 != 'N':
        print('Dados inválidos, por favor tente novamente!')
        op2 = input('Deseja continuar ? [S][N] ').upper().strip()
    if 'N' in op2:
        break

print('Obrigado, volte sempre.')







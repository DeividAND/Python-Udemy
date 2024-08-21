"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

lista_de_compras = []

while True:
    op = input('Selecione uma opção\n'
            '[i]nserir [a]pagar [l]istar: ').strip().upper()
    
    if op == 'I' :
        lista_de_compras.append(input('Digite o item que deseja adicionar a sua lista: '))
        print('Adicionado com sucesso!')

    elif op == 'A':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
            print('Deletado com sucesso!')
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif op == 'L':
        if len(lista_de_compras) == 0:
            print('Lista vazia adicione items.', lista_de_compras)
            continue
        else:
            for indice, valor in enumerate(lista_de_compras):
                print(f'{indice} - {valor}')

    else:
        print('Digite um opção válida!')
        continue

            
        
        
    

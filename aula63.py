"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario =re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_01 = 0
for digito_01 in nove_digitos:
    resultado_digito_01 += int(digito_01) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_01 = (resultado_digito_01 * 10) % 11
digito_01 = digito_01 if digito_01 <= 9 else 0
print(digito_01)

dez_digitos = nove_digitos + str(digito_01)
contador_regressivo_2 = 11

resultado_digito_02 = 0
for digito in dez_digitos:
    resultado_digito_02 +=  int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_02 = (resultado_digito_02 * 10) % 11
digito_02 = 0 if digito_02 > 9 else digito_02
print(digito_02)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_01}{digito_02}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')
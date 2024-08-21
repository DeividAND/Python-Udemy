import random
import sys

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

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
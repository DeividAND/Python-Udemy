cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += (int(digito) * contador_regressivo)
    contador_regressivo -= 1


digito_01 = (resultado * 10) % 11
digito_01 = digito_01 if digito_01 <= 9 else 0

print(digito_01)

cpf_digitado = str(input('Digite o CPF: '))

while len(cpf_digitado) != 11:
    print('Digite novamente!')
    cpf_digitado = str(input('Digite o CPF: '))


# Essa função converte a string em uma lista de números inteiros
def cpf_usuario(cpf):
    cpf_convertido = []
    for contagem in range(0, 11):
        cpf_convertido.append(int(cpf[contagem]))
    return cpf_convertido


# Essa função faz o cálculo dos ultimos 2 dígitos do CPF
def calculo_digito(decremento_valor, maximo_range, cpf):
    cpf_organizado = []
    decremento = decremento_valor
    for contagem in range(0, maximo_range):
        decremento = decremento - 1
        cpf_organizado.append(int(cpf[contagem]) * decremento)

    digito = 11 - ((sum(cpf_organizado)) % 11)
    if digito >= 10 or digito < 0:
        return 0
    return digito
# Será tratado para caso venha ocorrer algum erro
try:
    cpf = cpf_usuario(cpf_digitado)

    digito_verificador_um = calculo_digito(11, 9, cpf_digitado)

    digito_verificador_dois = calculo_digito(12, 10, cpf_digitado)

    if cpf[9] == digito_verificador_um and cpf[10] == digito_verificador_dois:
        print(f'CPF de número {cpf_digitado} é Valido!!!')
    else:
        print(f'CPF digitado não é valido!')

# Caso ocorra do usuário digitar letras/símbolos
except:
    print('Digite apenas números!')

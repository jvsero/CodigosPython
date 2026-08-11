# ============================================================
# FUNÇÃO 1 - CALCULAR UM DÍGITO VERIFICADOR DO CPF
# ============================================================

def calcular_cpf(digitos, peso_inicial):

    # Variável que vai armazenar a soma das multiplicações
    soma = 0

    # Primeiro peso utilizado no cálculo
    peso = peso_inicial

    # Percorre cada número recebido
    for numero in digitos:

        # Multiplica o número pelo peso correspondente
        soma += int(numero) * peso

        # Diminui o peso em 1
        peso -= 1

    # Calcula o resto da divisão
    resto = (soma * 10) % 11

    # Quando o resultado for 10, o dígito será 0
    if resto == 10:
        return 0

    # Retorna o dígito calculado
    return resto


# ============================================================a
# FUNÇÃO 2 - VALIDAR O CPF
# ============================================================

def validar_cpf(cpf):

    # Remove tudo que não for número
    # Exemplo:
    # 123.456.789-09 -> 12345678909
    apenas_numeros = "".join(
        filter(str.isdigit, str(cpf))
    )

    # Verifica se o CPF possui exatamente 11 dígitos
    if len(apenas_numeros) != 11:
        return False

    # Impede CPFs formados por números repetidos
    # Exemplos:
    # 11111111111
    # 22222222222
    # 99999999999
    if apenas_numeros == apenas_numeros[0] * 11:
        return False

    # --------------------------------------------------------
    # PRIMEIRO DÍGITO VERIFICADOR
    # --------------------------------------------------------

    # Pega os primeiros 9 números
    primeiros_9 = apenas_numeros[:9]

    # Calcula o primeiro dígito
    primeiro_digito = calcular_cpf(primeiros_9, 10)

    # O 10º número do CPF é o primeiro dígito verificador
    digito_informado_1 = int(apenas_numeros[9])

    # Compara o calculado com o informado
    if primeiro_digito != digito_informado_1:
        return False

    # --------------------------------------------------------
    # SEGUNDO DÍGITO VERIFICADOR
    # --------------------------------------------------------

    # Pega os 9 primeiros números
    # + o primeiro dígito calculado
    primeiros_10 = (
        apenas_numeros[:9] + str(primeiro_digito)
    )

    # Calcula o segundo dígito
    segundo_digito = calcular_cpf(primeiros_10, 11)

    # O 11º número do CPF é o segundo dígito verificador
    digito_informado_2 = int(apenas_numeros[10])

    # Compara o calculado com o informado
    if segundo_digito != digito_informado_2:
        return False

    # Se chegou até aqui, o CPF passou na validação
    return True


# ============================================================
# FUNÇÃO 3 - DESCOBRIR A REGIÃO FISCAL
# ============================================================

def descobrir_regiao(cpf):

    # Remove pontos, traços e outros caracteres
    apenas_numeros = "".join(
        filter(str.isdigit, str(cpf))
    )

    # Verifica se possui 11 dígitos
    if len(apenas_numeros) != 11:
        return "CPF inválido."

    # O 9º dígito do CPF indica a região fiscal
    # Como o Python começa a contar pelo índice 0,
    # o 9º dígito está no índice 8.
    digito_regiao = int(apenas_numeros[8])

    # Dicionário com as regiões fiscais
    regioes = {

        # Dígito 0
        0: "Rio Grande do Sul",

        # Dígito 1
        1: "Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins",

        # Dígito 2
        2: "Pará, Amazonas, Acre, Amapá, Rondônia e Roraima",

        # Dígito 3
        3: "Ceará, Maranhão e Piauí",

        # Dígito 4
        4: "Pernambuco, Rio Grande do Norte, Paraíba e Alagoas",

        # Dígito 5
        5: "Bahia e Sergipe",

        # Dígito 6
        6: "Minas Gerais",

        # Dígito 7
        7: "Rio de Janeiro e Espírito Santo",

        # Dígito 8
        8: "São Paulo",

        # Dígito 9
        9: "Paraná e Santa Catarina"
    }

    # Retorna a região correspondente
    return regioes[digito_regiao]


# ============================================================
# FUNÇÃO 4 - FORMATAR CPF
# ============================================================

def formatar_cpf(cpf):

    # Remove tudo que não for número
    cpf = "".join(
        filter(str.isdigit, str(cpf))
    )

    # Verifica se possui 11 dígitos
    if len(cpf) != 11:
        return "CPF inválido."

    # Monta o CPF no formato:
    # 000.000.000-00
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=" * 50)
print("              SISTEMA DE CPF")
print("=" * 50)

# Solicita o nome do usuário
nome=input("Digite o seu nome:")

# Solicita o CPF ao usuário
cpf = input("Digite o CPF: ")

print()
print(f"Nome do Titular do CPF: {nome}")
# Primeiro verificamos se o CPF é válido
if validar_cpf(cpf):

    print("CPF válido!")

    # Mostra o CPF formatado
    print("CPF formatado:", formatar_cpf(cpf))

    # Descobre a região fiscal
    print("Região fiscal:", descobrir_regiao(cpf))

else:

    print("CPF inválido!")

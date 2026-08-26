def palindromo():

    entrada = input("Digite uma palavra ou número: ")

    # Tratamento do campo da váriável "entrada" para descobrir o seu Tipo

    # O try e o except ValueError em Python fazem o tratamento de exceções (erros de execução) em blocos de código, e não o tratamento direto de uma função inteira por definição, embora possam envolver a chamada de uma função.

    try: # (Tentar): O Python executa o código que está dentro deste bloco. Se tudo correr bem, o programa ignora a parte do except

        valor = int(entrada)
        tipo = "int"

    except ValueError: # (Exceto Erro de Valor): Se o código do try gerar um erro do tipo ValueError, o programa não trava. Em vez disso, ele desvia o fluxo de execução para este bloco except

        try:

            valor = float(entrada)
            tipo = "float"

        except ValueError:

            valor = entrada
            tipo = "str"


    # O método .lower() converte todas as letras maiúsculas de uma string em minúsculas

    texto = entrada.lower()

    texto_limpo = ""

    # O metodo .isalnum() verifica se uma string é composta exclusivamente por caracteres alfanuméricos, ou seja, apenas letras (de A a Z) e/ou números (de 0 a 9).

    for caracter in texto:

        if caracter.isalnum():

            texto_limpo += caracter


    # Inverter usando o fatiamento em Python

    # Em Python, [::-1] inverte uma sequência, como uma string ou uma lista.

    # Como funciona o Fatiamento (Slicing) ---->[início:fim:passo]

    invertida = texto_limpo[::-1]


    # Mostra Resultado

    print("\n--------------------- Resultado ----------------------")

    print(f"Valor digitado: {entrada}")

    print(f"Tipo: {tipo}")

    print(f"Texto Analisado: {texto_limpo}")

    print(f"Texto Invertido: {invertida}")


    if texto_limpo == invertida:

        print("É um palíndromo!")

    else:

        print("Não é um palíndromo!")


palindromo()

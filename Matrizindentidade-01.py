def matriz_identidade():

    print("-"*30)

    print("MATRIZ DE IDENTIDADE")

    print("\n")

    print("A matriz identidade é uma matriz quadrada que tem:")
    print("- 1 na diagonal principal")
    print("- 0 em todas as outras posições")

    print("-"*30)

    print("\n")

    tamanho = int(input("Informe o tamanho da Matriz:" ))

    print("\n")

    matriz = []

    #for: "Para cada elemento/iteração de uma sequência, faça..."
    # while: "Enquanto esta condição for verdadeira, faça..."

    # i representa Linha
    # j representa coluna
    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)

        matriz.append(linha)

    for linha in matriz:
        print(linha)


matriz_identidade()
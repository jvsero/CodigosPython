def arvoreNatal():
    altura = 5

    # Copa da árvore
    for i in range(altura):

        # Espaços antes das estrelas
        for j in range(altura - i - 1):
            print(" ", end="")

        # Estrelas
        for j in range(2 * i + 1):
            print("*", end="")

        print()

    # Tronco
    for i in range(2):
        for j in range(altura - 2):
            print(" ", end="")

        print("|||")


# inspiração no link: https://dev.to/danielle8farias/construindo-uma-arvore-de-natal-com-python-57l6

arvoreNatal()

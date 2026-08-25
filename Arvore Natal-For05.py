def arvoreNatal():
    print("\n")
    print("-" * 60)
    print("\n")
    print("Árvore de Natal usando o for")
    print("\n")

    altura = 5

    print(" " * (altura - 1) + "º")

    # for "Para cada elemento/interação de uma sequência, faça ...(loop)"
    # I representa a minha Linha
    # range() serve para gerar uma sequência
    # Ex: range(altura), altura = 5 range é de 0 a 4

    for i in range(altura):
        espaco = " " * (altura - i - 1)
        estrela = "*" * (2 * i + 1)
        print(espaco + estrela)

    # Tronco da árvore

    print(" " * (altura - 2) + "|||")
    print(" " * (altura - 2) + "|||")


print("\n")
print("-" * 60)
print("\n")
print("Árvore de Natal usando o comando print")
print("\n")
print(" º")
print(" ***")
print(" *****")
print(" *******")
print("*********")
print(" |||")
print(" |||")
print("\n")

arvoreNatal()

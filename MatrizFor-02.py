
matriz = [
    [8, 3, 5],
    [1, 9, 4],
    [7, 2, 6]
]

print("\n")
# Recebe a entrada do usuário
numero_buscado = int(input("Digite um número para buscar: "))

encontrado = False

print("\n")
print("Matriz no formato visual:")
# Demostrar a minha matriz linha por linha no formato visual correto
for linha in matriz:
    print(linha)

# Percorre a matriz linha por linha
for linhas, linha in enumerate(matriz):
    for colunas, valor in enumerate(linha):
        if valor == numero_buscado:
# buscas na Matriz
            print("O valor está na Matriz:")
            print(linha)
            print(f"Encontrado na linha {linhas}")
            print(f"Encontrado na coluna {colunas}")
            print("\n")
            encontrado = True
            break 

if not encontrado:
    print("Número não encontrado na matriz.")

#Dados da Matriz
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
            encontrado = True
            break 

if not encontrado:
     print("Número não encontrado na matriz.")



linha=0
encontrado=False
while linha <len(matriz):
    coluna=0

    while coluna < len(matriz[linha]):

        if matriz[linha][coluna]==numero_buscado:
            print("\n")
            print("Número Inserido: ",numero_buscado)
            print("Número encontrado!")
            print("Linha:",   linha)
            print("Coluna:",  coluna)
            print("\n")
            encontrou = True

        coluna += 1

    linha += 1

if encontrou == False:
    print("Número não encontrado.")



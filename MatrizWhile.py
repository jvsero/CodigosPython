#Dados da Matriz
matriz = [
    [8, 3, 5],
    [1, 9, 4],
    [7, 2, 6]
]
print("\n")
print("Matriz no formato visual:")
# Demostrar a minha matriz linha por linha no formato visual correto
for linha in matriz:
    print(linha)

numero_procurado = 4

linha = 0
encontrou = False

while linha < len(matriz):

    coluna = 0

    while coluna < len(matriz[linha]):

        if matriz[linha][coluna] == numero_procurado:
            print("\n")
            print("Número Inserido: ",numero_procurado)
            print("Número encontrado!")
            print("Linha:",  linha)
            print("Coluna:", coluna)
            print("\n")
            encontrou = True

        coluna += 1

    linha += 1

if encontrou == False:
    print("Número não encontrado.")

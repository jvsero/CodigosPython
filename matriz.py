# Decobrir número em uma Matriz
matriz = [
    [8, 3, 5],
    [1, 9, 4],
    [7, 2, 6]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 9:
            print(f"Matriz Informada: {matriz}")
            print("Matriz Localizada:",matriz[i])
            print("O número esta na respectiva Linha:", [i])
            print("O número esta na respectiva Coluna:",[j])

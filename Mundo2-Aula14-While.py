# Estrutura de Repetição While

letra = input("Informe a variável: ")
repetir = int(input("Informe a quantidade de vezes a repetir: "))

quantidade = 0

while quantidade < repetir:
    print(quantidade, end=" ")
    quantidade += 1

print("\nFim")

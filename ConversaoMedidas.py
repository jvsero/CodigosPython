

'''
Escreva um programa que leia um valor de metros e o exiba convertido
em centímetros e milímetros
'''

# Função de Conversão
def converter_medidas(valor, origem, destino):

    # Converter Metros(m)
    if origem == "m" and destino == "cm":
        resultado = valor * 100

    elif origem == "m" and destino == "mm":
        resultado = valor * 1000

    # Converter Centímetros(cm)
    elif origem == "cm" and destino == "m":
        resultado = valor / 100

    elif origem == "cm" and destino == "mm":
        resultado = valor * 10

    # Converter Milímetros(mm)
    elif origem == "mm" and destino == "m":
        resultado = valor / 1000

    elif origem == "mm" and destino == "cm":
        resultado = valor / 10

    else:
        resultado = valor

    return resultado


# Menu
while True:

    print("\n")
    print("------------------------------------------------------------")
    print("Conversor de Medidas")
    print("------------------------------------------------------------")
    print("1 - Metros → Centímetros")
    print("2 - Metros → Milímetros")
    print("3 - Centímetros → Metros")
    print("4 - Centímetros → Milímetros")
    print("5 - Milímetros → Metros")
    print("6 - Milímetros → Centímetros")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("\nPrograma Encerrado!!")
        break

    elif opcao == "1":
        valor = float(input("Digite o valor em metros: "))
        resultado = converter_medidas(valor, "m", "cm")
        print(f"\n{valor} metros = {resultado:.2f} centímetros")

    elif opcao == "2":
        valor = float(input("Digite o valor em metros: "))
        resultado = converter_medidas(valor, "m", "mm")
        print(f"\n{valor} metros = {resultado:.2f} milímetros")

    elif opcao == "3":
        valor = float(input("Digite o valor em centímetros: "))
        resultado = converter_medidas(valor, "cm", "m")
        print(f"\n{valor} centímetros = {resultado:.2f} metros")

    elif opcao == "4":
        valor = float(input("Digite o valor em centímetros: "))
        resultado = converter_medidas(valor, "cm", "mm")
        print(f"\n{valor} centímetros = {resultado:.2f} milímetros")

    elif opcao == "5":
        valor = float(input("Digite o valor em milímetros: "))
        resultado = converter_medidas(valor, "mm", "m")
        print(f"\n{valor} milímetros = {resultado:.2f} metros")

    elif opcao == "6":
        valor = float(input("Digite o valor em milímetros: "))
        resultado = converter_medidas(valor, "mm", "cm")
        print(f"\n{valor} milímetros = {resultado:.2f} centímetros")

    else:
        print("\nOpção inválida! Digite uma opção de 0 a 6.")




import random
numeros = [ ]
mensagem = "    \n        Banca da Sorte          \n"
endereco = " Rua José Barreto S Sombra \n Centro Araripina-PE"
print(mensagem)
print(endereco)
print("\n")
print("---------------------------------------------------")
print("      Gerador de Números \n    ")

while len(numeros)<10:
    numero= random.randint(1,2000)
    numeros.append(numero)
    print(f"Número: {numero}")

print("\n Últimos 10 números chamados Banca da Sorte :  ")

for numero in numeros:
    print(numero)

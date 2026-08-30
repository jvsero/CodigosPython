''' Lê um número e informa a sua Tabuada'''
mensagem="DESCOBRINDO A TABUADA DE UM NÚMERO"
print("-"*20)
print(mensagem)
numero = int(input("Digite um número para ver a tabuada:"))
limite = int(input("Digite até onde deseja a tabuada: "))

print("\n")

# Repete de 1 até o limite informado
for tabuada in range(1, limite + 1):
    resultado = numero * tabuada
    print(f"{numero} x {tabuada} = {resultado}")
    



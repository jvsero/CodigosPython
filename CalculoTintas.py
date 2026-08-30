'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la.
Sabendo que cada litro de tinta pinta uma área de 2m²
'''

mensagem = "Desafio 11"

print(mensagem)
print("-" * 30)
print("\n")

largura = float(input("Largura da Parede: "))
altura = float(input("Altura da Parede: "))

print("\n")

area_parede = largura * altura

rendimento = 2
litros = area_parede / rendimento

print("-" * 30)
print("\n")

print("Informações:")
print(f"Largura: {largura:.2f} metros (m)")
print(f"Altura: {altura:.2f} metros (m)")
print(f"Área: {area_parede:.2f} metros quadrados (m²)")
print(f"Rendimento da tinta: {rendimento} m² por litro")
print(f"Quantidade de tinta necessária: {litros:.2f} litros (L)")

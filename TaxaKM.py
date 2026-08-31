"""
Desafio 15

Escreva um programa que pergunte a quantidade de KM percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado.

Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
e R$ 0,15 por KM rodado.
"""

cliente = input("Informe o cliente: ")
dias = int(input("Quantos dias alugados? "))
km_percorridos = float(input("Informe a quantidade de KM percorridos: "))
origem=input("Origem: ")
destino=input("Destino:  ")

valor_diarias = dias * 60
valor_km = km_percorridos * 0.15
valor_total = valor_diarias + valor_km

print("\n------------------ INFORMAÇÕES ------------------")
print("\n      COMPROVANTE             ")
print(f"Cliente: {cliente}")
print(f"Dias alugados: {dias}")
print(f"Origem: {origem}")
print(f"Destino: {destino}")
print(f"KM percorridos: {km_percorridos:.2f} km")
print(f"Valor das diárias: R$ {valor_diarias:.2f}")
print(f"Valor por KM: R$ {valor_km:.2f}")
print(f"Valor a pagar: R$ {valor_total:.2f}")

''' Crie um programa que leia quanto  dinheiro uma pessoa tem na carteira  e mostre quantos Dólares ela pode comprar.'''
print("----"*15)
print("CONVERSOR DE MOEDAS")
print("----"*15)

reais = float(input("Informe o valor do Real (R$): "))
cotacao = float(input("Informe a cotação do Dólar Comercial (US$): "))

dolares = reais / cotacao

print("\n")
print("--------------- RESULTADOS ---------------")
print(f"Investimento em Reais (R$): {reais:.2f}")
print(f"Cotação: US$ 1,00 vale R$ {cotacao:.2f}")
print(f"Valor total em Dólares (US$): {dolares:.2f}")

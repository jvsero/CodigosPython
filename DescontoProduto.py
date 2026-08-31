
# Desafio 12 Faça um algoritimo que leia o preço de umproduto e mostre seu preço com desconto

def desconto(descricao, preco, taxa):
    # Cálculo para o desconto
    valor_desconto = preco * taxa / 100

    # Cálculo do valor final
    valor_total = preco - valor_desconto

    print(f"\nAplicando taxa de {taxa:.2f}%")
    print("-------------- INFORMAÇÕES --------------")
    print(f"Produto: {descricao}")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Taxa de desconto: {taxa:.2f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")


# Entrada de Dados
descricao = input("Descrição do Produto: ")
preco = float(input("Informe o valor em R$: "))

taxa = input(
    "Informe o desconto (%) ou pressione ENTER para não aplicar o desconto: "
)

# Tratamento do desconto
if taxa == "":
    taxa = 0
else:
    taxa = float(taxa)


# Chamada da Função
desconto(descricao, preco, taxa)





# Desafio 13
# Faça um algoritmo que leia o salário de um funcionário  e mostre seu novo salário com o aumento.


def aumento(nome, cargo, salario, taxa):

    # Cálculo do aumento
    valor_aumento = salario * taxa / 100

    # Cálculo do novo salário
    valor_total = salario + valor_aumento

    print(f"\nAplicando taxa de aumento de {taxa:.2f}%")
    print("-------------- INFORMAÇÕES --------------")
    print(f"Funcionário: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Salário atual: R$ {salario:.2f}")
    print(f"Taxa de aumento: {taxa:.2f}%")
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"Novo salário: R$ {valor_total:.2f}")


# Entrada de Dados
nome = input("Funcionário: ")
cargo = input("Cargo: ")
salario = float(input("Informe o salário em R$: "))

taxa = input(
    "Informe a taxa de aumento (%) ou pressione ENTER para não aplicar o aumento: "
)

# Tratamento da taxa de aumento
if taxa == "":
    taxa = 0
else:
    taxa = float(taxa)


# Chamada da Função
aumento(nome, cargo, salario, taxa)



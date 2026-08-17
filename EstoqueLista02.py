

# Lista que armazenará os produtos
estoque = []

# Função de Cadastrar Produtos

def cadastrar_produto():

    print("\n===== CADASTRAR PRODUTO =====")

    nome = input("Digite o nome do produto: ")

    preco = float(input("Digite o preço do produto: R$ "))

    quantidade = int(input("Digite a quantidade em estoque: "))

    # Criando uma lista para representar o produto
    produto = [nome, preco, quantidade]

    # Adicionando o produto na lista estoque
    estoque.append(produto)

    print("\nProduto cadastrado com sucesso!")


# Função de Consultar todos Produtos


def consultar_produtos():

    print("\n===== ESTOQUE =====")

    if len(estoque) == 0:
        print("O estoque está vazio.")
        return

    for i, produto in enumerate(estoque):

        print(f"\nCódigo: {i}")
        print(f"Produto: {produto[0]}")
        print(f"Preço: R$ {produto[1]:.2f}")
        print(f"Quantidade: {produto[2]}")


# Função de Consultar Produto

def consultar_produto():

    print("\n===== CONSULTAR PRODUTO =====")

    nome_busca = input("Digite o nome do produto: ")

    encontrado = False

    for produto in estoque:

        if produto[0].lower() == nome_busca.lower():

            print("\nProduto encontrado!")
            print(f"Nome: {produto[0]}")
            print(f"Preço: R$ {produto[1]:.2f}")
            print(f"Quantidade: {produto[2]}")

            encontrado = True

    if encontrado == False:
        print("\nProduto não encontrado.")


# Função de Alterar Produtos

def alterar_produto():

    print("\n===== ALTERAR PRODUTO =====")

    nome_busca = input("Digite o nome do produto: ")

    for produto in estoque:

        if produto[0].lower() == nome_busca.lower():

            print("\nProduto encontrado!")

            novo_nome = input("Digite o novo nome: ")

            novo_preco = float(
                input("Digite o novo preço: R$ ")
            )

            nova_quantidade = int(
                input("Digite a nova quantidade: ")
            )

            produto[0] = novo_nome
            produto[1] = novo_preco
            produto[2] = nova_quantidade

            print("\nProduto alterado com sucesso!")

            return

    print("\nProduto não encontrado.")


# Função de Excluir Cadastrar Produtos

def excluir_produto():

    print("\n===== EXCLUIR PRODUTO =====")

    nome_busca = input("Digite o nome do produto: ")

    for produto in estoque:

        if produto[0].lower() == nome_busca.lower():

            estoque.remove(produto)

            print("\nProduto excluído com sucesso!")

            return

    print("\nProduto não encontrado.")


# Menu Principal
while True:

    print("\n================================")
    print("       SISTEMA DE ESTOQUE")
    print("================================")

    print("1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("3 - Consultar produto")
    print("4 - Alterar produto")
    print("5 - Excluir produto")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        cadastrar_produto()

    elif opcao == "2":

        consultar_produtos()

    elif opcao == "3":

        consultar_produto()

    elif opcao == "4":

        alterar_produto()

    elif opcao == "5":

        excluir_produto()

    elif opcao == "0":

        print("\nSistema encerrado.")

        break

    else:

        print("\nOpção inválida!")

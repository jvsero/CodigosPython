
estoque = []


# Cadastrar Produtos


def cadastrar_produto():

    nome = input("Digite o nome do produto: ")

    preco = float(input("Digite o preço do produto: R$ "))

# Criando dicionário 
    produto = {
        "nome": nome,
        "preco": preco
    }

    estoque.append(produto)

    print("\nProduto cadastrado com sucesso!")

    # Localizar Produtos

def localizar_produto():
    busca=input("Digite o nome do produto:")
    encontrado = False

    for produto in estoque:    
        if produto["nome"].lower()==busca.lower():
             print("\nProduto encontrado!")
             print("Nome:", produto["nome"])
             print(f"Preço: R$ {produto['preco']:.2f}")
    encontrado = True

# Alterar produto

def alterar_produto():
    busca =input("Digite o nome do produto:")
    encontrado = False

    for produto in estoque:
        if produto["nome"].lower()==busca.lower():

            encontrado = True

            print("\nProduto encontrado!")
            print("1 - Alterar nome")
            print("2 - Alterar preço")
            print("3 - Alterar nome e preço")

# Opções da Tela
            opcao=input("Escolha uma opção:")

            if opcao == "1":
                novo_nome=input("Digite o nome o novo nome:")
                produto["nome"]=novo_nome

                print("\n Nome alterado com sucesso!")

            elif opcao == "2":
                novo_preco=float(input("Digite o novo preco:R$"))
                produto["preco"]=novo_preco

                print("\n Preço alterad com sucesso!")

            elif opcao == "3":

                novo_nome = input("Digite o novo nome: ")

                novo_preco = float(
                    input("Digite o novo preço: R$ ")
                )

                produto["nome"] = novo_nome
                produto["preco"] = novo_preco

                print("\nProduto alterado com sucesso!")

            else:

                print("\nOpção inválida.")

    if not encontrado:
        print("\nProduto não encontrado.")



#Excluir Produtos

def excluir_produto():

    busca = input("Digite o nome do produto que deseja excluir: ")

    encontrado = False

    for produto in estoque:

        if produto["nome"].lower() == busca.lower():

            estoque.remove(produto)

            encontrado = True

            print("\nProduto excluído com sucesso!")

            break

    if not encontrado:
        print("\nProduto não encontrado.")


# Lista de Estoque
def listar_estoque():

    if len(estoque) == 0:

        print("\nEstoque vazio.")

    else:

        print("\n========== ESTOQUE ==========")

        for produto in estoque:

            print(
                f"Produto: {produto['nome']} | "
                f"Preço: R$ {produto['preco']:.2f}"
            )



# Menu principal

while True:

    print("\n")
    print("========== CONTROLE DE ESTOQUE ==========")
    print("1 - Cadastrar produto")
    print("2 - Localizar produto")
    print("3 - Alterar produto")
    print("4 - Excluir produto")
    print("5 - Listar estoque")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        cadastrar_produto()

    elif opcao == "2":

        localizar_produto()

    elif opcao == "3":

        alterar_produto()

    elif opcao == "4":

        excluir_produto()

    elif opcao == "5":

        listar_estoque()

    elif opcao == "0":

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida.")

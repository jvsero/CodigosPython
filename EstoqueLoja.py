# Variável global
estoque = []

# Função auxiliar para encontrar o menor código disponível (reaproveita excluídos)
def obter_proximo_codigo():
    codigos_em_uso = {produto["codigo"] for produto in estoque}
    codigo = 1
    while codigo in codigos_em_uso:
        codigo += 1
    return codigo

# Função de Cadastro de Produtos
def cadastrar_produto(marca, modelo, preco, cor, quantidade):
    codigo = obter_proximo_codigo()
    
    produto = {
        "codigo": codigo,
        "marca": marca,
        "modelo": modelo,
        "cor": cor,
        "preco": preco,  
        "quantidade": quantidade
    }
    estoque.append(produto)
    print(f"\nProduto Cadastrado com Sucesso! Código gerado: {codigo}")

# Busca do Produto por Código
def localizar_produto():
    try:
        busca_codigo = int(input("Informe o código do produto: "))
    except ValueError:
        print("\nCódigo inválido! Digite apenas números.")
        return

    encontrado = False
    for produto in estoque:
        if produto["codigo"] == busca_codigo:
            print("\nProduto encontrado!")
            print("Código:", produto["codigo"])
            print("Marca:", produto["marca"])
            print("Modelo:", produto["modelo"])
            print("Cor:", produto["cor"])
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("Qtde:", produto["quantidade"])
            encontrado = True
            break

    if not encontrado:
        print("\nProduto não encontrado.")

# Alterar produto por Código
def alterar_produto():
    try:
        busca_codigo = int(input("Digite o código do produto que deseja alterar: "))
    except ValueError:
        print("\nCódigo inválido! Digite apenas números.")
        return

    encontrado = False
    for produto in estoque:
        if produto["codigo"] == busca_codigo:
            encontrado = True
            print(f"\nProduto encontrado (Código: {produto['codigo']})!")
            print("1 - Alterar Marca")
            print("2 - Alterar Modelo")
            print("3 - Alterar Cor e Preço")
            print("4 - Alterar Quantidade")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                produto["marca"] = input("Digite a nova Marca: ")
                print("\nMarca alterada com sucesso!")
            elif opcao == "2":
                produto["modelo"] = input("Digite o novo Modelo: ")
                print("\nModelo alterado com sucesso!")
            elif opcao == "3":
                produto["cor"] = input("Digite a nova Cor: ")
                produto["preco"] = float(input("Digite o novo Preço: R$ "))
                print("\nCor e Preço alterados com sucesso!")
            elif opcao == "4":
                produto["quantidade"] = int(input("Digite a nova Quantidade: "))
                print("\nQuantidade alterada com sucesso!")
            else:
                print("\nOpção inválida.")
            break

    if not encontrado:
        print("\nProduto não encontrado.")

# Função de Excluir Produtos por Código
def excluir_produto():
    try:
        busca_codigo = int(input("Digite o código do produto que deseja excluir: "))
    except ValueError:
        print("\nCódigo inválido! Digite apenas números.")
        return

    encontrado = False
    for produto in estoque:
        if produto["codigo"] == busca_codigo:
            estoque.remove(produto)
            encontrado = True
            print(f"\nProduto de código {busca_codigo} excluído com sucesso!")
            print("Este código está livre para o próximo cadastro.")
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
                f"Código: {produto['codigo']} | "
                f"Marca: {produto['marca']} | "
                f"Modelo: {produto['modelo']} | "
                f"Cor: {produto['cor']} | "
                f"Preço: R$ {produto['preco']:.2f} | "
                f"Qtde: {produto['quantidade']}"
            )

# Menu principal
while True:
    print("\n========== CONTROLE DE ESTOQUE ==========")
    print("1 - Cadastrar produto")
    print("2 - Localizar produto por Código")
    print("3 - Alterar produto por Código")
    print("4 - Excluir produto por Código")
    print("5 - Listar estoque")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        marca_in = input("Marca: ")
        modelo_in = input("Modelo: ")
        cor_in = input("Cor: ")
        preco_in = float(input("Preço: R$ "))
        quantidade_in = int(input("Quantidade: "))

        cadastrar_produto(
            marca=marca_in,
            modelo=modelo_in,
            preco=preco_in,
            cor=cor_in,
            quantidade=quantidade_in
        )

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

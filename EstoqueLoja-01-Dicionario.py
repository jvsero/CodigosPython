# 'estoque' é uma lista global que armazenará todos os dicionários de produtos.
estoque = []


# Colocar Pârametros 

def obter_proximo_codigo():
    
    # Cria um conjunto com os códigos já em uso (variável local)
    codigos_em_uso = {produto["codigo"] for produto in estoque}
    
    codigo = 1
    # Incrementa até encontrar o primeiro número que NÃO está em uso
    while codigo in codigos_em_uso:
        codigo += 1
        
    return codigo


def cadastrar_produto(marca, modelo, preco_unitario, cor, quantidade):
   
    # Obtenção do código disponível
    codigo = obter_proximo_codigo()
    
    # Calcula o preço total do produto
    preco_total = preco_unitario * quantidade
    
    # Dicionário representando o produto (variável local)
    produto = {
        "codigo": codigo,
        "marca": marca,
        "modelo": modelo,
        "cor": cor,
        "preco_unitario": preco_unitario,
        "preco_total": preco_total,
        "quantidade": quantidade
    }
    
    # Adiciona o dicionário à lista global 'estoque'
    estoque.append(produto)
    print(f"\nProduto Cadastrado com Sucesso! Código gerado: {codigo}")


def localizar_produto():
    """
    Solicita o código do produto e realiza a busca sequencial no estoque.
    Utiliza bloco try/except para validar a entrada numérica.
    """
    try:
        busca_codigo = int(input("Informe o código do produto: "))
    except ValueError:
        print("\nCódigo inválido! Digite apenas números.")
        return

    encontrado = False
    
    # Loop de busca no estoque
    for produto in estoque:
        if produto["codigo"] == busca_codigo:
            print("\nProduto encontrado!")
            print("Código:", produto["codigo"])
            print("Marca:", produto["marca"])
            print("Modelo:", produto["modelo"])
            print("Cor:", produto["cor"])
            print(f"Preço unitário: R$ {produto['preco_unitario']:.2f}")
            print("Qtde:", produto["quantidade"])
            print(f"Preço total: R$ {produto['preco_total']:.2f}")
            encontrado = True
            break  # Interrompe o loop ao encontrar o produto

    if not encontrado:
        print("\nProduto não encontrado.")


def alterar_produto():
    """
    Busca o produto pelo código e exibe um submenu para alterar.
    """
    try:
        busca_codigo = int(input("Digite o código do produto que deseja alterar: "))
    except ValueError:
        print("\nCódigo inválido! Digite apenas números.")
        return

    encontrado = False
    
    # Busca o item para alteração
    for produto in estoque:
        if produto["codigo"] == busca_codigo:
            encontrado = True
            print(f"\nProduto encontrado (Código: {produto['codigo']})!")
            print("1 - Alterar Marca")
            print("2 - Alterar Modelo")
            print("3 - Alterar Cor e Preço")
            print("4 - Alterar Quantidade")

            opcao = input("Escolha uma opção: ")

            # Atualização dos campos do dicionário
            if opcao == "1":
                produto["marca"] = input("Digite a nova Marca: ")
                print("\nMarca alterada com sucesso!")

            elif opcao == "2":
                produto["modelo"] = input("Digite o novo Modelo: ")
                print("\nModelo alterado com sucesso!")

            elif opcao == "3":
                produto["cor"] = input("Digite a nova Cor: ")

                try:
                    produto["preco_unitario"] = float(
                        input("Digite o novo Preço Unitário: R$ ")
                    )

                    produto["preco_total"] = (
                        produto["preco_unitario"] * produto["quantidade"]
                    )

                    print("\nCor e Preço alterados com sucesso!")

                except ValueError:
                    print("\nPreço inválido! Digite apenas números.")

            elif opcao == "4":
                try:
                    produto["quantidade"] = int(
                        input("Digite a nova Quantidade: ")
                    )

                    produto["preco_total"] = (
                        produto["preco_unitario"] * produto["quantidade"]
                    )

                    print("\nQuantidade alterada com sucesso!")

                except ValueError:
                    print("\nQuantidade inválida! Digite apenas números.")

            else:
                print("\nOpção inválida.")
            break

    if not encontrado:
        print("\nProduto não encontrado.")


def excluir_produto():
    """
    Remove o dicionário do produto da lista 'estoque' usando o código.
    Libera o código para reutilização em futuros cadastros.
    """
    try:
        busca_codigo = int(input("Digite o código do produto que deseja excluir: "))
    except ValueError:
        print("\nCódigo inválido! Digite apenas números.")
        return

    encontrado = False
    
    for produto in estoque:
        if produto["codigo"] == busca_codigo:
            estoque.remove(produto)  # Remove o dicionário da lista global
            encontrado = True
            print(f"\nProduto de código {busca_codigo} excluído com sucesso!")
            print("Este código está livre para o próximo cadastro.")
            break

    if not encontrado:
        print("\nProduto não encontrado.")


def listar_estoque():
    """
    Percorre a lista 'estoque' e exibe os dados formatados de todos os produtos.
    """
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
                f"Preço unitário: R$ {produto['preco_unitario']:.2f} | "
                f"Qtde: {produto['quantidade']} | "
                f"Preço total: R$ {produto['preco_total']:.2f}"
            )


# Menu  Principal
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
        # Coleta das entradas do usuário em variáveis locais
        marca_input = input("Marca: ")
        modelo_input = input("Modelo: ")
        cor_input = input("Cor: ")

        try:
            preco_unitario_input = float(input("Preço Unitário: R$ "))
            quantidade_input = int(input("Quantidade: "))

            if preco_unitario_input < 0:
                print("\nO preço não pode ser negativo.")
                continue

            if quantidade_input < 0:
                print("\nA quantidade não pode ser negativa.")
                continue

        except ValueError:
            print("\nValor inválido! Digite números corretamente.")
            continue

        # Chamada da função utilizando parâmetros nomeados (keyword arguments)
        cadastrar_produto(
            marca=marca_input,
            modelo=modelo_input,
            preco_unitario=preco_unitario_input,
            cor=cor_input,
            quantidade=quantidade_input
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
        break  # Encerra o loop 'while' e finaliza o programa

    else:
        print("\nOpção inválida.")


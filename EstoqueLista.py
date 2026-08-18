#Uso dos método .upper() transforma todas as letras de um texto em maiúsculas, enquanto o .strip() apaga os espaços vazios que ficam no começo e no final do texto.


from datetime import datetime
agora = datetime.now()





estoque = []

# Contador para gerar o ID automaticamente
proximo_id = 1

# Função Cadastra Produtos

def cadastrar_produtos():

    global proximo_id

    print("\n========== CADASTRAR PRODUTOS ==========")

    nome = input("Digite o nome do produto: ").strip()
# Atribuir a escolha do tipo do Produto
    print("\nComo o produto é vendido?")
    print("1 - Unidade")
    print("2 - Peso")
    print("3 - Fardo")
#Escolha do Tipo para armazena na lista de ESTOQUE
    tipo = int(input("Escolha: "))

    if tipo == 1:

        quantidade = int(input("Quantidade de Unidades (UN): "))
        tipo = "UN"

    elif tipo == 2:

        quantidade = float(input("Quantidade em Quilos (Kg): "))
        tipo = "KG"

    elif tipo == 3:

        quantidade = int(input("Quantidade de Fardos (FD): "))
        tipo = "FD"

    else:
        print("Opção inválida!")
        return
       

    preco = float(input("Digite o preço unitário: "))

    categoria = input("Digite a categoria: ").strip()

    # Valor total do produto em estoque
    estoque_total = preco * quantidade

    # ID automático
    id_produto = proximo_id

    proximo_id += 1

    # Criando a variavél produto para armazena as informações na lista de ESTOQUE
    produto = [
        id_produto,
        nome,
        preco,
        tipo,
        quantidade,
        categoria,
        estoque_total
    ]

    # Adicionando o produto ao estoque
    estoque.append(produto)

    # Mostra Produto Cadastrado

    print("\nProduto cadastrado com sucesso!\n")

    print("Informações do Produto Cadastrado:")

    print(f"ID: {id_produto}")
    print(f"Nome: {nome}")
    print(f"Tipo: {tipo}")
    print(f"Quantidade: {quantidade}")
    print(f"Categoria: {categoria}")
    print(f"Preço Unitário: R$ {preco:.2f}")
    print(f"Estoque Atual: R$ {estoque_total:.2f}")

#Função Consultar Produto
def consulta_produtos():

    print("\n========== CONSULTAR PRODUTOS ==========")

    if len(estoque)==0:
        print("Nenhum produto cadastrado")
        return
#Percorrer a lista de ESTOQUE
    for produto in estoque:
        print("-----------------------------------------------------")

        print("\n========== PRODUTO ==========")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Preço: R$ {produto[2]:.2f}")
        print(f"Tipo: {produto[3]}")
        print(f"Quantidade: {produto[4]}")
        print(f"Categoria: {produto[5]}")
        print(f"Valor em estoque: R$ {produto[6]:.2f}")

        print("-----------------------------------------------------")
# #Função Consultar Estoque
def consultar_estoque():
    print("\n========== ESTOQUE ==========")
#Realizar a contagem de ESTOQUE
    if len(estoque)==0:
        print("Estoque Vázio.")
        return

    valor_total_estoque=0

    for produto in estoque:
        id_produto=produto[0]
        nome=produto[1]
        preco=produto[2]
        tipo = produto[3]
        quantidade = produto[4]
        categoria = produto[5]
        valor = produto[6]

        valor_total_estoque += valor

        print("----------------------------------")

        print(f"ID: {id_produto}")
        print(f"Nome: {nome}")
        print(f"Preço: R$ {preco:.2f}")
        print(f"Tipo: {tipo}")
        print(f"Quantidade: {quantidade}")
        print(f"Categoria: {categoria}")
        print(f"Valor: R$ {valor:.2f}")

        print("----------------------------------")

    print(f"VALOR TOTAL DO ESTOQUE: R$ {valor_total_estoque:.2f}")
# Função Alterar Produto
def alterar_produto():
#Realizar a contagem de ESTOQUE
    if len(estoque)==0:
        print("Nenhum Produto foi encontrado.")
        return
# id_busca é responsavél por buscar o produto
    id_busca=int(input("Digite o ID do produto que deseja alterar: "))
     #Percorrer a lista de ESTOQUE
    for produto in estoque:
        if produto[0]==id_busca:
            print("\nProduto encontrado!")

            print(f"ID: {produto[0]}")
            print(f"Nome atual:  {produto[1]}")
            print(f"Preço atual:  R$ {produto[2]:.2f}")
            print(f"Tipo atual:  {produto[3]}")
            print(f"Quantidade atual:  {produto[4]}")
            print(f"Categoria atual:  {produto[5]}")

# Alterar toda caracteristica  do Produto para depois armazena na lista de ESTOQUE

            print("\nDigite os novos dados.")

# Configurar novo nome ,unidade,tipo,preço etc.. para o produto.
            nome=input("Novo nome:").strip()

            print("\nNovo tipo:")
            print("1-Unidade")
            print("2-Peso")
            print("3-Fardo")
# Atribuir a escolha do tipo do Produto para armazena na lista de ESTOQUE
            tipo=int(input("Escolha:"))

            if tipo==1:
                quantidade=int(input("Nova qtde.Unidade: "))
                tipo="UN"

            elif tipo==2:
                quantidade=float(input("Nova qtde.KG: "))
                tipo="KG"

            elif tipo==3:
                quantidade=int(input("Nova qtde.Fardos "))
                tipo="FD"
            else:
                print("Tipo inválido.")
                return
#Definir novo preço a ser alterado
            preco=float(input("Novo preco: "))
#Definir uma nova categoria ao produto            
            categoria=input("Nova categoria:  ").strip()
#Recalcula o valor total do estoque após alterar o produto

#Realiza a alteração dos DADOS da lista de Produtos
            estoque_total=preco*quantidade
            produto[1]=nome
            produto[2]=preco
            produto[3]=tipo
            produto[4]=quantidade
            produto[5]=categoria
            produto[6]=estoque_total

            print("ATENÇÃO !!!!")
            print("Produto cadastrado com sucesso!")

#Função para Excluir Produto
def excluir_produto():
    print("\n========== EXCLUIR PRODUTO ==========")

    if len(estoque)==0:
        print("Nenhum produto cadastrado.")
        return
# id_busca é responsavél por buscar o produto
    id_busca=int(input("Digite o ID do Produto que deseja excluir: "))
# Ele vai percorrer a lista de Estoque
    for produto in estoque:
        if produto[0]==id_busca:
             print("\nProduto encontrado!")
             print(f"ID: {produto[0]}")
             print(f"Nome: {produto[1]}")
             print(f"Quantidade: {produto[4]} {produto[3]}")

             confirmacao=input(
                 "ATENÇÃO!! Tem certeza que quer excluir? (S/N):"
             ).upper()
# Menu de Escolha entre Sim ou Não para remover o produto.
        if confirmacao=='S':
            estoque.remove(produto)
#Informações do produto que foi excluído da Lista de ESTOQUE
            print("\nINFORMAÇÕES SOBRE PRODUTO EXCLUÍDO")
            print("\nProduto encontrado!")
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            

            print("\nProduto excluido com Sucesso!!")

        else:
             print("\nExclusão cancelada.")
             return
        print("Produto não encontrado.")

#Função Menu

def menu():
    while True:
        print("\n")
        print("======================================")
        print("          SISTEMA DE ESTOQUE")
        print("======================================")
        print("1 - Cadastrar produto")
        print("2 - Consultar produtos")
        print("3 - Consultar estoque")
        print("4 - Alterar produto")
        print("5 - Excluir produto")
        print("0 - Sair")
        print("======================================")

        opcao=input("Escolha uma opção: ")

        if opcao=="1":
            cadastrar_produtos()

        elif opcao=="2":
            consulta_produtos()

        elif opcao=="3":
            consultar_estoque()

        elif opcao=="4":
            alterar_produto()

        elif opcao=="5":
            excluir_produto()

        elif opcao=="0":
            print("\nSistema encerrado.")
            break

        else:
             print("\nOpção inválida!")




#Definir Mensagem
def mensagem():

    mensagem = (
    "Olá! Seja Bem Vindo(a) JVS Super\n"
    f"Confira as ofertas do Supermercado para hoje {agora}\n"
    )

    return mensagem


print("\n")
# Mensagem
print(mensagem())
# Iniciar o Menu
menu()







                        









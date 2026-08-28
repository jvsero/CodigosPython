estoque=[]
'''
proximo_codigo=1 uma variável que guarda a próximo número indentificação.
'''
proximo_codigo = 1

'''
Função  def gerar_codigo(): para gerar um código autómático
'''
def gerar_codigo():
    global proximo_codigo

    codigo=proximo_codigo
    proximo_codigo += 1

    return codigo

'''
Função para cadastrar carro
'''
def cadastrar_veiculos():
    print("\n========= CADASTRAR VEìCULOS ==========")

    marca=input("Digete a marca: ")
    modelo=input("Digite o modelo: ")
    cor=input("Digite a cor: ")
    ano=input("Digite o Ano: ")

    preco_unitario=float(input("Digite o preço unitário:R$ "))
    quantidade=int(input("Digite a quantidade: "))

   # Cálculo para adicionar o valor total do produto ao estoque
    preco_total=preco_unitario * quantidade

    codigo = gerar_codigo()

    veiculos={
        "codigo":codigo,
        "marca": marca,
        "modelo":modelo,
        "ano":ano,
        "cor":cor,
        "preco_unitario":preco_unitario,
        "quantidade":quantidade,
        "preco_total":preco_total
    }

    estoque.append(veiculos)
    print("\n Carro cadastrado com sucesso!")
    print(f"\nCódigo do veículo:{codigo}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R$ {preco_total:.2f}")


    '''
      Função para Pesquisar o Veículo
      A principal função do .strip() é remover todos os espaços em branco

       encontrado = False Isso significa: ““Ainda não encontrei nenhum carro.”.”
    
    
    '''
def pesquisar_veiculo():
    print("\n ========= PESQUISAR VEìCULOS ==========")
    pesquisa=input("Digite o código ou a descrição do Veículo: ").strip()
    encontrado=False

    '''
    
    Para cada elemento(veículo) que existe dentro do uma coleção (estoque) faça alguma coisa.”
    
    '''

    for veiculo in estoque:
        codigo=str(veiculo["codigo"])
        descricao=(
            f'{veiculo["marca"]} '
            f'{veiculo["modelo"]} '
            f'{veiculo["ano"]} '
            f'{veiculo["cor"]}'
        )

        '''
        O método .lower() em Python transforma todas as letras maiúsculas de um texto (string) em letras minúsculas.

        pesquisa.lower() transforma o texto em letras minúsculas.
        in pergunta:“Esse texto está dentro desse outro texto?” este resultado é True ou é False.

        or em Python é um operador lógico que significa "ou". Ele une duas ou mais condições e retorna True (verdadeiro) se pelo menos uma das partes for verdadeira. Só retorna False se tudo for falso.

        encontrado = True Isso significa: “Encontrei pelo menos um carro.”

        if not encontrado: Inverter o valor lógico de True para False e vice-verce.
  
        
        '''

        if pesquisa.lower() in codigo.lower() or pesquisa.lower() in descricao.lower():

            print("\n-------------------------------------")
            print(f'Código: {veiculo["codigo"]}')
            print(f'Marca: {veiculo["marca"]}')
            print(f'Modelo: {veiculo["modelo"]}')
            print(f'Ano: {veiculo["ano"]}')
            print(f'Cor: {veiculo["cor"]}')
            print(f'Preço unitário: R$ {veiculo["preco_unitario"]:.2f}')
            print(f'Quantidade: {veiculo["quantidade"]}')
            print(f'Preço total: R$ {veiculo["preco_total"]:.2f}')
            print("----------------------------------------")

            encontrado=True

    if not encontrado:
        print("\n Veículo não encontrado.")    

'''
Função para Alterar o Veículo

Para cada elemento(veículo) que existe dentro do uma coleção (estoque) faça alguma coisa.”

encontrados.append(carro) Ou seja:coloque esse Veículo dentro da lista encontrados

 if not encontrado: Inverter o valor lógico de True para False e vice-verce.

  veiculo_selecionado = None, o None significa:“Nenhum valor foi encontrado/selecionado neste momento.” É como colocar uma etiqueta:CARRO SELECIONADO:ainda nenhum 

'''    

def alterar_veiculos():
    print("\n ========= ALTERAR VEìCULOS ==========")

    pesquisar=input("Digite o código ou a descrição do veículo: ").strip()

    encontrados=[]

    for veiculo in estoque:
        codigo=str(veiculo["codigo"])

        descricao=(
            f'{veiculo["marca"]} '
            f'{veiculo["modelo"]} '
            f'{veiculo["ano"]} '
            f'{veiculo["cor"]}'
        )

        if pesquisar.lower() in codigo.lower() or pesquisar.lower() in descricao.lower():

            encontrados.append(veiculo)

    if not encontrados:
        print("\n Véiculo não encontrado")
        return

    if len(encontrados)>1:
        print("\nForam enconrados vários veículos.")

        for veiculo in encontrados:
            print(
                f'Código: {veiculo["codigo"]} | '
                f'Veículo: {veiculo["marca"]} {veiculo["modelo"]} | '
                f'Ano: {veiculo["ano"]}'
            )

        codigo_escolhido=input("Digite o código do veículo que deseja alterar: ")

        veiculo_selecionado = None

        for veiculo in encontrados:
            if str(veiculo["codigo"])==codigo_escolhido:
                veiculo_selecionado=veiculo
                break

        if veiculo_selecionado is None:
            print("\n código não encontrado.")
            return

        veiculo=veiculo_selecionado

    else:
        veiculo=encontrados[0]

    print("\nPressione ENTER para manter o valor atual.")

    nova_marca=input(f'Marca [{veiculo["marca"]}]:')  

    novo_modelo=input(f'Modelo [{veiculo["modelo"]}]: ')

    novo_ano=input(f'Ano [{veiculo["ano"]}]: ')

    nova_cor=input(f'Cor [{veiculo["cor"]}]: ')

    novo_preco = input(
        f'Preço unitário [{veiculo["preco_unitario"]:.2f}]: R$ '
    )

    nova_quantidade = input(
        f'Quantidade [{veiculo["quantidade"]}]: '
    )


    if nova_marca:
        veiculo["marca"] = nova_marca

    if novo_modelo:
        veiculo["modelo"] = novo_modelo

    if novo_ano:
        veiculo["ano"] = novo_ano

    if nova_cor:
        veiculo["cor"] = nova_cor

    if novo_preco:
        veiculo["preco_unitario"] = float(novo_preco)

    if nova_quantidade:
        veiculo["quantidade"] = int(nova_quantidade)

    veiculo["preco_total"] = (
        veiculo["preco_unitario"] * veiculo["quantidade"]
    )

    print("\nCarro alterado com sucesso!")
    print(f"Preço unitário: R$ {veiculo['preco_unitario']:.2f}")
    print(f"Quantidade: {veiculo['quantidade']}")
    print(f"Preço total: R$ {veiculo['preco_total']:.2f}")



'''
Função para excluir Veículos 

'''

def excluir_veiculos():
    print("\n========== EXCLUIR VEÍCULOS ==========")

    pesquisa = input(
        "Digite o código ou a descrição do carro: "
    ).strip()

    encontrados = []

    for veiculo in estoque:

        codigo = str(veiculo["codigo"])

        descricao = (
            f'{veiculo["marca"]} '
            f'{veiculo["modelo"]} '
            f'{veiculo["ano"]} '
            f'{veiculo["cor"]}'
        )

        if pesquisa.lower() in codigo.lower() or \
           pesquisa.lower() in descricao.lower():

            encontrados.append(veiculo)

    if not encontrados:
        print("\nCarro não encontrado.")
        return

    if len(encontrados) > 1:

        print("\nForam encontrados vários carros:")

        for veiculo in encontrados:
            print(
                f'Código:  {veiculo["codigo"]} | '
                f'Veículo: {veiculo["marca"]} {veiculo["modelo"]} | '
                f'Ano: {veiculo["ano"]}'
            )

        codigo_escolhido = input(
            "\nDigite o código do carro que deseja excluir: "
        )

        veiculo = None

        for item in encontrados:
            if str(item["codigo"]) == codigo_escolhido:
                veiculo = item
                break

        if veiculo is None:
            print("\nCódigo não encontrado.")
            return

    else:
        veiculo = encontrados[0]

    print("\nCarro encontrado:")
    print(
        f'{veiculo["codigo"]} - '
        f'{veiculo["marca"]} '
        f'{veiculo["modelo"]} - '
        f'R$ {veiculo["preco_total"]:.2f}'
    )

    confirmacao = input(
        "Deseja realmente excluir? (S/N): "
    ).upper()

    if confirmacao == "S":

        estoque.remove(veiculo)

        print("\nCarro excluído com sucesso!")

    else:
        print("\nExclusão cancelada.")


'''
Função para  Visualização do Estoque 

'''

def visualizar_estoque():
    print("\n========== ESTOQUE DE VEÍCULOS ==========")

    if not estoque:
        print("\nO estoque está vazio.")
        return

    for veiculo in estoque:

        print("\n----------------------------------------")
        print(f'Código          : {veiculo["codigo"]}')
        print(f'Marca           : {veiculo["marca"]}')
        print(f'Modelo          : {veiculo["modelo"]}')
        print(f'Ano             : {veiculo["ano"]}')
        print(f'Cor             : {veiculo["cor"]}')
        print(f'Preço unitário  : R$ {veiculo["preco_unitario"]:.2f}')
        print(f'Quantidade      : {veiculo["quantidade"]}')
        print(f'Preço total     : R$ {veiculo["preco_total"]:.2f}')
        print("----------------------------------------")

    print(f"\nTotal de carros no estoque: {len(estoque)}")


# ============================================
# MENU
# ============================================

def menu():

    while True:

        print("\n========================================")
        print("       LOJA DE CARROS & Motos ")
        print("========================================")
        print("1 - Cadastrar ")
        print("2 - Pesquisar ")
        print("3 - Alterar ")
        print("4 - Excluir ")
        print("5 - Visualizar estoque")
        print("0 - Sair")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_veiculos()

        elif opcao == "2":
            pesquisar_veiculo()

        elif opcao == "3":
            alterar_veiculos()

        elif opcao == "4":
            excluir_veiculos()

        elif opcao == "5":
            visualizar_estoque()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida!")


# iniciar

menu()


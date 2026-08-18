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

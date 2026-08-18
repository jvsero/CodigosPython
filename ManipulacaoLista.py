# Controle de estoque de Supermecado

mensagem= "Seja Bem-Vindo \n Supermercado Saga Senai"
print(mensagem)
produtos=[]

print("Estoque de Produtos")
while True:
    produto=input("Digite o nome do produto: ")

    if produto == "sair":
        print(f"Estoque Atual: {produtos}")
        break

    elif produto == "remover":
        produto_remover=input("Digite o produto a remover: ")
        produtos.remove(produto_remover)
    else:
        produtos.append(produto)

    print(produtos)





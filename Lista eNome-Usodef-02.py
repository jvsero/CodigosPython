lista_convidados = ["Emily", "Neilma", "Joel"]
print("Lista Original: ", lista_convidados)
print("-" * 30)

def verifica_nome_na_lista(nome):
    if nome in lista_convidados:
        return True
    else:
        return False

def cadastro_nome():
    nome_digitado = input("Informe o novo nome: ")
    
    pessoa_ja_cadastrada = verifica_nome_na_lista(nome_digitado)
    
    if pessoa_ja_cadastrada:
        print("Pessoa já cadastrada!")
    else:
        print("Pessoa não cadastrada! Adicionando à lista...")
        lista_convidados.append(nome_digitado)
        print("Novo nome adicionado: ", nome_digitado)
    
    print(f"\nLista Atualizada: {lista_convidados}")

cadastro_nome()

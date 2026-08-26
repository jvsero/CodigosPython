lista_convidados=["Emily","Neilma","Joel"]
# Definir função para Verificar se o nome se encontra na Lista
def verifica_nome_na_lista(nome):
    if nome in lista_convidados:
        return True
    else:
        return False

nome_existe_na_lista=verifica_nome_na_lista("Joel")

if nome_existe_na_lista:
    print("Acesso Liberado")

else:
    print("Acesso Negado!")


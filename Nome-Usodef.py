# Uso de def no Python server  serve para definir ou criar uma função, que é um bloco de código reutilizável para realizar uma tarefa específica

mensagem="Olá Seja Bem Vindo!"
nome=input("Digite o seu nome: ")
idade=int(input("Informe sua idade:"))
print(mensagem)

def mostra_infor(nome_p,idade_p):
    print(f"Oi {nome}")
    print(f"Uh é mesmo sua idade é {idade} anos?")
   
mostra_infor(nome,idade)

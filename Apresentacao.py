'''
O def __init__ em Python funciona como o método construtor de uma classe, sendo executado automaticamente sempre que um novo objeto é criado.
Sua principal função é inicializar os atributos do objeto, definindo valores iniciais ou configurando o estado básico que o objeto terá ao nascer no código.
'''

class Pessoa:
    # O método _init_ é o construtor que inicializa os atributos
    def __init__(self,nome,idade):
        self.nome=nome #Atributo nome
        self.idade=idade # Atributos idade
    # Um método(ação)que o objeto executa
    def apresentar(self):
        print( f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
# Entrada de Dados
nome=input("Digite o seu nome:")
idade=int(input("Idade: "))

#pessoa é meu objeto
pessoa=Pessoa(nome,idade)
# paresentar() é o meu método
pessoa.apresentar()


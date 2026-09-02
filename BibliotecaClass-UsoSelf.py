
'''
QUESTÃO

Uma pequena biblioteca de uma escola atualmente controla seus empréstimos de livros
manualmente. Para melhorar esse processo, a direção solicitou a criação de um
programa em Python que permita cadastrar livros e controlar quando eles estão
disponíveis ou emprestados.

O sistema deverá representar cada livro como um objeto. Cada Livro deve possuir:
    • Título;
    • Autor;
    • Situação que poderá ser disponível ou emprestado.

O programa também deverá permitir que o livro seja emprestado e posteriormente
devolvido.

Um livro que já esteja emprestado não poderá ser emprestado. Da mesma forma,
somente um livro que esteja emprestado poderá ser devolvido.


Situação-problema:

Você ficou responsável pelo desenvolvimento desse sistema. Utilizando os
conceitos de Programação:

a) Crie uma classe Livro com os atributos necessários.
b) Crie métodos para realizar o empréstimo e a devolução de um livro.
c) Garanta que o livro emprestado não possa ser emprestado novamente.
d) Crie pelo menos três objetos da classe Livro.
e) Realize alguns empréstimos e devoluções exibindo ao final a situação de cada Livro.

Ao realizar, explique brevemente quais elementos do programa representam a
classe, objetos, atributos e métodos.
'''



# Classe Livro
class Livro:

    # Atributos da classe
    titulo = ""
    autor = ""
    situacao = "Disponível"

    # Método para emprestar o livro
    def emprestar(self):

        # Verifica se o livro está disponível
        if self.situacao == "Disponível":

            # Altera a situação do livro para emprestado
            self.situacao = "Emprestado"

            print(f'O livro "{self.titulo}" foi emprestado.')

        else:

            # Caso o livro já esteja emprestado
            print(f'O livro "{self.titulo}" já está emprestado.')

    # Método para devolver o livro
    def devolver(self):

        # Verifica se o livro está emprestado
        if self.situacao == "Emprestado":

            # Altera a situação do livro para disponível
            self.situacao = "Disponível"

            print(f'O livro "{self.titulo}" foi devolvido.')

        else:

            # Caso o livro já esteja disponível
            print(f'O livro "{self.titulo}" já está disponível.')

    # Método para exibir as informações
    def exibir(self):

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Situação: {self.situacao}")
        print("-" * 30)

# Criação dos Objetos


livro1 = Livro()
livro2 = Livro()
livro3 = Livro()
livro4 = Livro()

# Definindo os Atributos dos Objetos


livro1.titulo = "Dom Casmurro"
livro1.autor = "Machado de Assis"
livro1.situacao = "Disponível"

livro2.titulo = "O Pequeno Príncipe"
livro2.autor = "Antoine de Saint-Exupéry"
livro2.situacao = "Disponível"

livro3.titulo = "Harry Potter e a Pedra Filosofal"
livro3.autor = "J. K. Rowling"
livro3.situacao = "Disponível"

livro4.titulo = "O Auto da Compadecida"
livro4.autor = "Ariano Suassuna"
livro4.situacao = "Disponível"


# ============================================
# REALIZANDO OS EMPRÉSTIMOS
# ============================================

livro1.emprestar()
livro3.emprestar()

# Tentando emprestar novamente o livro 1
livro1.emprestar()


# ============================================
# REALIZANDO AS DEVOLUÇÕES
# ============================================

livro1.devolver()

# Tentando devolver novamente o livro 1
livro1.devolver()


# ============================================
# EMPRESTANDO NOVAMENTE
# ============================================

livro4.emprestar()


# ============================================
# SITUAÇÃO FINAL DOS LIVROS
# ============================================

print("\nSITUAÇÃO FINAL DOS LIVROS")
print("=" * 30)

livro1.exibir()
livro2.exibir()
livro3.exibir()
livro4.exibir()



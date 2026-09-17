```python
# Importa a biblioteca tkinter.
#
# "tkinter" é uma biblioteca do Python usada
# para criar interfaces gráficas (janelas,
# botões, campos de texto, etiquetas etc.).
#
# "as tk" significa que vamos chamar tkinter
# pelo apelido "tk".
#
# Exemplo:
# tkinter.Label()
#
# passa a ser:
# tk.Label()

import tkinter as tk


# ==========================================================
# CLASS CALCULADORA
# ==========================================================
#
# Aqui estamos criando uma CLASS chamada Calculadora.
#
# Pense em uma class como uma "estrutura" ou "molde"
# que reúne os dados e as funções da nossa calculadora.
#
# Dentro dela teremos:
#
# - os campos dos números
# - os botões
# - a operação escolhida
# - o resultado
# - as funções que fazem os cálculos
#
class Calculadora:


    # ======================================================
    # __init__
    # ======================================================
    #
    # O __init__ é um método especial.
    #
    # Ele é executado automaticamente quando criamos
    # um objeto da class Calculadora.
    #
    # Exemplo no final do programa:
    #
    # calculadora = Calculadora(janela)
    #
    # Nesse momento o Python entra automaticamente
    # neste __init__.
    #
    # "self" representa o objeto da calculadora.
    #
    # "janela" é a janela que estamos passando para
    # dentro da class.
    #
    def __init__(self, janela):


        # ==================================================
        # CONFIGURAÇÃO DA JANELA
        # ==================================================

        # Guarda a janela dentro do objeto.
        #
        # self.janela significa:
        #
        # "a janela pertencente a esta calculadora".
        #
        # Isso permite utilizar a janela em outros
        # métodos da class.
        #
        self.janela = janela


        # Define o título da janela.
        #
        # A barra superior da janela mostrará:
        #
        # Calculadora
        #
        self.janela.title("Calculadora")


        # Define o tamanho da janela.
        #
        # 500 = largura
        # 350 = altura
        #
        # Portanto:
        #
        # 500 pixels de largura
        # 350 pixels de altura
        #
        self.janela.geometry("500x350")


        # Impede que o usuário redimensione a janela.
        #
        # False = não permite alterar o tamanho.
        #
        self.janela.resizable(False, False)


        # ==================================================
        # OPERAÇÃO PADRÃO
        # ==========================
```

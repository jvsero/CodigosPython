from tkinter import*
# Atribuir a biblioteca  tkinter o apelido 'tk'.
import tkinter as tk

janela = tk.Tk()
# Título da janela
janela.title("Calculadora")
# Tamanho da Janela Largura e Altura
janela.geometry("350x500")


'''
Usa-se o .resizable(False,False) manter o tamanho da janela Fixa 
O primeiro False controla a Largura
O segundo False controla a Altura
Então o False não pode Alterar já o True pode Alterar

'''
janela.resizable(False,False)


'''
O StringVar() criar uma variável do Tkinter.
Agora display será responsável pelo texto mostrado no visor.
'''
display=tk.StringVar()



'''

 Entry (input) usado para entrar no texto.
 O usuário não deverá digitar diretamente no visor. Os números serão colocados através dos botões.

'''
visor=tk.Entry(
    janela,textvariable=display
    )

'''grid() responsavél pela estrutura de Linhas e Colunas

        coluna
          ↓
       0   1   2   3

linha 0 ┌───┬───┬───┬───┐
        │   │   │   │   │
        ├───┼───┼───┼───┤
linha 1 │ 7 │ 8 │ 9 │ ÷ │
        ├───┼───┼───┼───┤
linha 2 │ 4 │ 5 │ 6 │ × │
        ├───┼───┼───┼───┤
linha 3 │ 1 │ 2 │ 3 │ - │
        ├───┼───┼───┼───┤
linha 4 │ 0 │ C │ = │ + │
        └───┴───┴───┴───┘

'''



'''
Frame() funciona como um container 
'''
tk.Frame()







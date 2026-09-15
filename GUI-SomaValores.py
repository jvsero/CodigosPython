
import tkinter as tk

from tkinter import messagebox


# Cria a Janela

janela = tk.Tk()

janela.title("Soma de dois números")

janela.geometry("300x250")


# Janela referente ao Número 1

tk.Label(janela, text="Número 1:").pack()


# Input (Entrada) relacionada ao Número 1

numero1 = tk.Entry(janela)

numero1.pack()


# Número 2

tk.Label(janela, text="Número 2:").pack()


# Input (Entrada) relacionada ao Número 2

numero2 = tk.Entry(janela)

numero2.pack()


# Função que realiza a soma

def somar():

    n1 = float(numero1.get())

    n2 = float(numero2.get())

    resultado = n1 + n2

    label_resultado.config(text=f"Resultado: {resultado}")


# Criar o botão

tk.Button(janela, text="SOMAR", command=somar).pack(pady=20)


# Resultado

label_resultado = tk.Label(janela, text="Resultado:")

label_resultado.pack()


# Mantém a janela aberta

janela.mainloop()


# Importa a biblioteca tkinter
# Ela permite criar a interface gráfica.
import tkinter as tk


# Cria a janela principal
janela = tk.Tk()


# Define o título da janela
janela.title("Soma de dois valores")


# Define o tamanho da janela
janela.geometry("350x300")


# Impede que o usuário altere o tamanho da janela
janela.resizable(False, False)


# ==================================================
# TÍTULO
# ==================================================

titulo = tk.Label(
    janela,
    text="Soma de dois valores",
    font=("Arial", 20, "bold")
)

titulo.pack(pady=20)


# ==================================================
# PRIMEIRO VALOR
# ==================================================

label1 = tk.Label(
    janela,
    text="Digite o primeiro valor:",
    font=("Arial", 12)
)

label1.pack()


# Campo onde o usuário vai digitar o primeiro número
numero1 = tk.Entry(
    janela,
    font=("Arial", 16),
    justify="center"
)

numero1.pack(
    pady=5
)


# ==================================================
# SEGUNDO VALOR
# ==================================================

label2 = tk.Label(
    janela,
    text="Digite o segundo valor:",
    font=("Arial", 12)
)

label2.pack(
    pady=(10, 0)
)


# Campo onde o usuário vai digitar o segundo número
numero2 = tk.Entry(
    janela,
    font=("Arial", 16),
    justify="center"
)

numero2.pack(
    pady=5
)


# ==================================================
# FUNÇÃO SOMAR
# ==================================================

def somar():

    # Pega o valor digitado no primeiro campo
    valor1 = numero1.get()

    # Pega o valor digitado no segundo campo
    valor2 = numero2.get()

    # Converte os valores de texto para números
    valor1 = float(valor1)
    valor2 = float(valor2)

    # Realiza a soma
    resultado = valor1 + valor2

    # Mostra o resultado na tela
    resultado_label.config(
        text=f"Resultado: {resultado}"
    )


# ==================================================
# BOTÃO SOMAR
# ==================================================

botao = tk.Button(
    janela,
    text="SOMAR",
    font=("Arial", 14, "bold"),
    command=somar
)

botao.pack(
    pady=15
)


# ==================================================
# RESULTADO
# ==================================================

resultado_label = tk.Label(
    janela,
    text="Resultado: 0",
    font=("Arial", 18, "bold")
)

resultado_label.pack()


# ==================================================
# INICIAR A INTERFACE
# ==================================================

# mainloop() mantém a janela aberta
# e fica esperando o usuário interagir.
janela.mainloop()

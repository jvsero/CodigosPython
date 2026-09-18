import tkinter as tk
from tkinter import messagebox



class ConversorTemperatura(tk.Tk):

    def __init__(self):
        """
        super().__init__() chama o construtor da classe pai (tk.Tk).
        Isso permite reutilizar o código da classe pai.
        """
        super().__init__()

        # Configuração da janela
        self.title("Conversor de Temperatura")
        self.geometry("500x400")
        self.resizable(False, False)

        # Menu
        
        # Título
        self.label_titulo = tk.Label(
            self,
            text="Celsius para Fahrenheit",
            font=("Arial", 12, "bold")
        )
        self.label_titulo.pack(pady=10)

        # Texto explicativo
        self.label_celsius = tk.Label(
            self,
            text="Digite a temperatura em ºC:"
        )
        self.label_celsius.pack()

        # Campo para digitar a temperatura
        self.entrada_celsius = tk.Entry(
            self,
            font=("Arial", 11),
            justify="center"
        )
        self.entrada_celsius.pack(pady=5)

        # Botão de conversão
        self.botao_converter = tk.Button(
            self,
            text="Converter",
            command=self.converter,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.botao_converter.pack(pady=10)

        # Rótulo que mostrará o resultado
        self.label_resultado = tk.Label(
            self,
            text="Resultado:",
            font=("Arial", 11)
        )
        self.label_resultado.pack(pady=5)

    def converter(self):
        try:
            # Pega o texto digitado no Entry
            celsius = float(self.entrada_celsius.get())

            # Fórmula:
            # Fahrenheit = (Celsius × 9/5) + 32
            fahrenheit = (celsius * 9 / 5) + 32

            # Mostra o resultado na tela
            self.label_resultado.config(
                text=f"Resultado: {fahrenheit:.2f} °F"
            )

        except ValueError:
            # Aparece caso o usuário digite letras ou deixe vazio
            messagebox.showerror(
                "Erro",
                "Por favor, digite um número válido!"
            )


# Inicia o programa
if __name__ == "__main__":
    app = ConversorTemperatura()
    app.mainloop()

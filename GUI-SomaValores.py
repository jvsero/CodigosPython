
import tkinter as tk


class Calculadora:

    def __init__(self, janela):

        # ==========================================
        # CONFIGURAÇÃO DA JANELA
        # ==========================================

        self.janela = janela
        self.janela.title("Calculadora")
        self.janela.geometry("500x350")
        self.janela.resizable(False, False)

        # Guarda a operação escolhida
        self.operacao = "+"

        # ==========================================
        # TÍTULO
        # ==========================================

        titulo = tk.Label(
            janela,
            text="Calculadora",
            font=("Arial", 26, "bold")
        )

        titulo.pack(pady=20)

        # ==========================================
        # LINHA DOS INPUTS
        # ==========================================

        frame_calculo = tk.Frame(janela)
        frame_calculo.pack(pady=10)

        # ------------------------------------------
        # INPUT 1
        # ------------------------------------------

        self.input1 = tk.Entry(
            frame_calculo,
            font=("Arial", 20),
            width=8,
            justify="center"
        )

        self.input1.grid(
            row=0,
            column=0,
            padx=10
        )

        # Quando o usuário digitar,
        # chama a função calcular()
        self.input1.bind(
            "<KeyRelease>",
            self.calcular
        )

        # ------------------------------------------
        # SINAL DA OPERAÇÃO
        # ------------------------------------------

        self.sinal = tk.Label(
            frame_calculo,
            text="+",
            font=("Arial", 25, "bold"),
            width=3
        )

        self.sinal.grid(
            row=0,
            column=1
        )

        # ------------------------------------------
        # INPUT 2
        # ------------------------------------------

        self.input2 = tk.Entry(
            frame_calculo,
            font=("Arial", 20),
            width=8,
            justify="center"
        )

        self.input2.grid(
            row=0,
            column=2,
            padx=10
        )

        # Quando o usuário digitar,
        # chama a função calcular()
        self.input2.bind(
            "<KeyRelease>",
            self.calcular
        )

        # ==========================================
        # BOTÕES DAS OPERAÇÕES
        # ==========================================

        frame_operacoes = tk.Frame(janela)
        frame_operacoes.pack(pady=20)

        # Botão +
        tk.Button(
            frame_operacoes,
            text="+",
            font=("Arial", 18, "bold"),
            width=4,
            command=lambda: self.escolher_operacao("+")
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        # Botão -
        tk.Button(
            frame_operacoes,
            text="-",
            font=("Arial", 18, "bold"),
            width=4,
            command=lambda: self.escolher_operacao("-")
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        # Botão *
        tk.Button(
            frame_operacoes,
            text="*",
            font=("Arial", 18, "bold"),
            width=4,
            command=lambda: self.escolher_operacao("*")
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        # Botão /
        tk.Button(
            frame_operacoes,
            text="/",
            font=("Arial", 18, "bold"),
            width=4,
            command=lambda: self.escolher_operacao("/")
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        # ==========================================
        # RESULTADO
        # ==========================================

        tk.Label(
            janela,
            text="Resultado",
            font=("Arial", 16, "bold")
        ).pack(pady=(10, 5))

        self.resultado = tk.Label(
            janela,
            text="0",
            font=("Arial", 30, "bold")
        )

        self.resultado.pack()

    # ==========================================
    # ESCOLHER OPERAÇÃO
    # ==========================================

    def escolher_operacao(self, operacao):

        # Guarda a operação escolhida
        self.operacao = operacao

        # Mostra o sinal entre os dois inputs
        self.sinal.config(text=operacao)

        # Calcula automaticamente
        self.calcular()

    # ==========================================
    # CALCULAR
    # ==========================================

    def calcular(self, evento=None):

        # Pega o valor do primeiro input
        valor1 = self.input1.get()

        # Pega o valor do segundo input
        valor2 = self.input2.get()

        # Se algum campo estiver vazio,
        # não realiza o cálculo
        if valor1 == "" or valor2 == "":
            self.resultado.config(text="0")
            return

        try:

            # Converte os valores para número
            numero1 = float(valor1)
            numero2 = float(valor2)

            # --------------------------------------
            # SOMA
            # --------------------------------------

            if self.operacao == "+":
                resultado = numero1 + numero2

            # --------------------------------------
            # SUBTRAÇÃO
            # --------------------------------------

            elif self.operacao == "-":
                resultado = numero1 - numero2

            # --------------------------------------
            # MULTIPLICAÇÃO
            # --------------------------------------

            elif self.operacao == "*":
                resultado = numero1 * numero2

            # --------------------------------------
            # DIVISÃO
            # --------------------------------------

            elif self.operacao == "/":

                if numero2 == 0:
                    self.resultado.config(text="Não é possível dividir por 0")
                    return

                resultado = numero1 / numero2

            # Mostra o resultado automaticamente
            self.resultado.config(text=resultado)

        except ValueError:

            # Caso o usuário digite algo
            # que não seja um número
            self.resultado.config(text="Digite números válidos")


# ==============================================
# INICIAR O PROGRAMA
# ==============================================

janela = tk.Tk()

calculadora = Calculadora(janela)

janela.mainloop()

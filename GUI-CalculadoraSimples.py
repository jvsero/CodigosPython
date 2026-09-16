
# IMPORTANDO A BIBLIOTECA TKINTER

import tkinter as tk

class Calculadora:


    def __init__(self):

       
        # CRIANDO A JANELA PRINCIPAL
        # ----------------------------------------------------

        # tk.Tk() cria a janela principal do programa.
        self.janela = tk.Tk()

        # Define o título da janela.
        self.janela.title("Calculadora Simples")

        # Define o tamanho inicial da janela.
        self.janela.geometry("360x520")

        # Impede que o usuário redimensione a janela.
        self.janela.resizable(False, False)

        # Define a cor de fundo da janela.
        self.janela.configure(bg="#1e1e2f")


        
        # CRIANDO O VISOR
       
        # StringVar é uma variável especial do tkinter.
        # Ela permite colocar e alterar textos dentro
        # de componentes da interface.

        self.valor = tk.StringVar()

        # Começamos o visor mostrando "0".
        self.valor.set("0")

        # CRIANDO O CAMPO DO VISOR   

        self.visordisplay = tk.Entry(
            self.janela,

            # Ligamos o Entry à variável self.valor.
            textvariable=self.valor,

            # Tamanho da fonte.
            font=("Arial", 28, "bold"),

            # Alinhamento do texto à direita.
            justify="right",

            # Cor do texto.
            fg="white",

            # Cor de fundo.
            bg="#292940",

            # Remove a borda.
            bd=0,

            # Espaçamento interno.
            insertbackground="white"
        )

        # Posicionamos o visor na janela ou seja ele serve para posicionar e dimensionar o visor da calculadora dentro da janela.

        '''
        padx=20	Espaço externo nas laterais
        pady=30	Espaço externo em cima e embaixo
        fill="x"	Expande horizontalmente
        ipady=15	Aumenta o espaço interno vertical


                     VISOR
               │
       ┌───────┴───────┐
       │               │
       │  ipady        │ ← espaço INTERNO
       │               │
       └───────────────┘
        ↑             ↑
       padx          padx
        ←─── 20 ────→

             ↑
            pady
             ↓
        
        '''
        self.visordisplay.pack(
            padx=20,
            pady=30,
            fill="x",
            ipady=15
        )

     
        # CRIANDO A ÁREA DOS BOTÕES
        
        # Frame é como se fosse uma "caixa".

        self.frame_botoes = tk.Frame(
            self.janela,
            bg="#1e1e2f"
        )

        self.frame_botoes.pack(
            padx=15,
            pady=10,
            fill="both",
            expand=True
        )

        # CRIANDO OS BOTÕES
        # Primeiro vamos criar uma lista contendo os botões.

        botoes = [
            ("C", 0, 0),
            ("/", 0, 1),
            ("*", 0, 2),
            ("-", 0, 3),

            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("+", 1, 3),

            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("=", 2, 3),

            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),

            ("0", 4, 0),
            (".", 4, 1),
        ]

       
        # PERCORRENDO A LISTA DE BOTÕES
        

        for texto, linha, coluna in botoes:

            # Definimos uma cor padrão para os botões.
            cor = "#3b3b55"

            # Botão "C" terá uma cor diferente.
            if texto == "C":
                cor = "#e74c3c"

            # Botões das operações terão outra cor.
            elif texto in ["/", "*", "-", "+", "="]:
                cor = "#6c5ce7"

            
            # CRIANDO O BOTÃO
           
            botao = tk.Button(

                self.frame_botoes,

                # Texto que aparece no botão.
                text=texto,

                # Tamanho e estilo da fonte.
                font=("Arial", 18, "bold"),

                # Cor do texto.
                fg="white",

                # Cor de fundo.
                bg=cor,

                # Remove a borda.
                bd=0,

                # Altura do botão.
                height=2,

                # Comando que será executado quando
                # o usuário clicar.
                command=lambda valor=texto:
                    self.clique_botao(valor)
            )

            
            #POSICIONANDO O BOTÃO
           

            botao.grid(
                row=linha,
                column=coluna,

                # Espaçamento entre os botões.
                padx=5,
                pady=5,

                # Faz o botão ocupar o espaço disponível.
                sticky="nsew"
            )

        '''
        
        CONFIGURANDO AS COLUNAS
        Temos 4 colunas.weight=1 faz as colunas dividirem o espaço igualmente.
        
        '''

        for coluna in range(4):
            self.frame_botoes.columnconfigure(
                coluna,
                weight=1
            )

        #  CONFIGURANDO AS LINHAS

        for linha in range(5):
            self.frame_botoes.rowconfigure(
                linha,
                weight=1
            )

     # FUNÇÃO DOS BOTÕES
    # Esta função será executada sempre que um botão for pressionado.

    def clique_botao(self, botao):

        
        #  BOTÃO LIMPAR
       
        if botao == "C":

            # Apaga o conteúdo do visor.
            self.valor.set("0")

        #  BOTÃO IGUAL
       

        elif botao == "=":

            try:

                # Pegamos o que está escrito no visor.
                expressao = self.valor.get()

                # eval() calcula a expressão matemática.
                resultado = eval(expressao)

                # Mostramos o resultado no visor.
                self.valor.set(str(resultado))

            except:

                # Se ocorrer algum erro, mostramos "Erro".
                self.valor.set("Erro")


        # NÚMEROS E OPERADORES
        else:

            # Pegamos o conteúdo atual do visor.
            atual = self.valor.get()

            # Se o visor estiver mostrando "0",
            # substituímos pelo botão pressionado.

            if atual == "0":
                self.valor.set(botao)

            else:

                # Caso contrário, adicionamos o novo
                # caractere ao final do visor.

                self.valor.set(
                    atual + botao
                )



# CRIANDO O OBJETO DA CLASSE
# "Calculadora()" cria um objeto baseado na classe Calculadora.

calculadora = Calculadora()

# INICIANDO A INTERFACE
# mainloop() mantém a janela aberta.Sem essa linha, a janela abriria e fecharia imediatamente.

calculadora.janela.mainloop()

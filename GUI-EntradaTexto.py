
# Importa a biblioteca tkinter
import tkinter as tk


# Cria a classe Calculadora
class Calculadora:

    def __init__(self, master):

        # Guarda a janela (master) principal dentro do objeto
        self.master = master

        # Define o título da janela
        self.master.title("Calculadora")

        # Define o tamanho da janela
        self.master.geometry("300x400")

        # Define a cor de fundo da janela
        self.master.config(bg="#fcfcff")

        
        # EXPRESSÃO MATEMÁTICA
        '''
         Aqui vamos armazenar a conta que o usuário está digitando.
        Exemplo:
            usuário aperta 5
            self.expressao = "5"
            depois aperta +
            self.expressao = "5+"
            depois aperta 2
            self.expressao = "5+2"
        '''
        self.expressao = ""

        
        # VISOR DA CALCULADORA
        '''
        StringVar é uma variável especial do tkinter.
        Ela permite controlar o texto que aparece no Entry.
        '''
        self.visor = tk.StringVar()

        # Cria o campo que funciona como visor
        self.entrada = tk.Entry(
            self.master,

            # Liga o Entry à variável self.visor
            textvariable=self.visor,

            # Define o tipo e tamanho da fonte
            font=("Arial", 20),

            # Espessura da borda
            bd=10,

            # Tamanho do cursor
            insertwidth=4,

            # Largura do campo
            width=14,

            # Espessura da borda
            borderwidth=4,

            # Alinha o texto à direita
            justify="right"
        )

        '''
        Posiciona o visor na janela:
                
                row=0 primeira linha
                column=0 primeira coluna
                columnspan=4 ocupa 4 colunas
                padx=10espaço horizontal externo
                pady=20 espaço vertical externo
        
        
        
        '''
        self.entrada.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=20
        )

        # Chama o método responsável por criar os botões
        self.criar_botoes()

   
    # MÉTODO PARA CRIAR OS BOTÕES
    '''
    Lista contendo:
             texto do botão
             linha
             coluna
            
            Exemplo:('7', 2, 0)
            significa:
            botão com texto "7"
            linha 2
            coluna 0
    
    
    
    '''

    def criar_botoes(self):


        botoes = [
            ("C", 1, 0),
            ("(", 1, 1),
            (")", 1, 2),
            ("/", 1, 3),

            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("*", 2, 3),

            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("-", 3, 3),

            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("+", 4, 3),

            ("0", 5, 0),
            (".", 5, 1),
            ("=", 5, 2)
        ]

        '''
        Percorre todos os botões da lista
                texto  = texto do botão
                linha  = posição da linha
                coluna = posição da coluna
        
        
        '''
        for texto, linha, coluna in botoes:

            # Verifica se o botão é o botão "="
            if texto == "=":

                # Cria o botão =
                btn = tk.Button(
                    self.master,

                    # Texto que aparece no botão
                    text=texto,

                    # Fonte do botão
                    font=("Arial", 14),

                    # Largura do botão
                    width=11,

                    # Altura do botão
                    height=2,

                    # Quando clicar, chama clique_botao()
                    #
                    # t=texto guarda o texto do botão
                    # para evitar problemas com o lambda
                    command=lambda t=texto: self.clique_botao(t)
                )

                # Coloca o botão na janela
                #
                # columnspan=2 faz o botão ocupar
                # duas colunas
                btn.grid(
                    row=linha,
                    column=coluna,
                    columnspan=2,
                    padx=2,
                    pady=2
                )

            else:

                # Cria os outros botões
                btn = tk.Button(
                    self.master,
                    text=texto,
                    font=("Arial", 14),
                    width=5,
                    height=2,

                    # Quando clicar no botão,
                    # chama o método clique_botao()
                    command=lambda t=texto: self.clique_botao(t)
                )

                # Posiciona o botão
                btn.grid(
                    row=linha,
                    column=coluna,
                    padx=2,
                    pady=2
                )

    
    # MÉTODO PARA TRATAR O CLIQUE DOS BOTÕES
    

    def clique_botao(self, valor):

        # Verifica se o usuário clicou no botão "="
        if valor == "=":

            try:

                '''
                eval() interpreta a expressão matemática.
                Exemplo: self.expressao = "5+2"
                eval("5+2")
                resultado = 7
                
                '''
                resultado = eval(self.expressao)

                # Converte o resultado para texto
                self.expressao = str(resultado)

                # Mostra o resultado no visor
                self.visor.set(self.expressao)

            except:

                # Caso exista algum erro na expressão, mostramos "Erro"
                self.visor.set("Erro")

                # Limpa a expressão
                self.expressao = ""

        # Verifica se o usuário clicou no botão "C"
        elif valor == "C":

            # Limpa a expressão
            self.expressao = ""

            # Limpa o visor
            self.visor.set("")

        # Caso não seja "=" nem "C"
        else:

            self.expressao += str(valor)

            # Atualiza o visor
            self.visor.set(self.expressao)


# PROGRAMA PRINCIPAL
# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":

    # Cria a janela principal do tkinter
    root = tk.Tk()

    # Cria um objeto da classe Calculadora
    app = Calculadora(root)

    # Mantém a janela aberta
    root.mainloop()

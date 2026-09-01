class Livros:
    # O metodo _init_ é o construtor de classe
     def __init__(self, titulo, autor,ano):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        sel.disponivel=True
    # Método para exibir as informações do Livro
    
class AcervoLivros:
    """Classe responsável por armazenar e listar múltiplos livros."""
    def __init__(self):
        self.lista_livros = []  # Armazenará as instâncias concretas de Veiculo

    def cadastrar_Livros(self,titulo, autor,ano):
        # Cria um novo objeto Livro e adiciona à lista
        novo_livro = Livros(titulo, autor,ano)
        self.lista_livros.append(novo_livro)
    
    def descricao(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} ({self.ano}) - Status: {status}"
        
        
        
        

    

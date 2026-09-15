
class Funcionario:

    def __init__(self, nome: str, cpf: str, salario: float):
        self.nome = nome
        self.cpf = cpf
        self.salario_bruto = salario

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Salário bruto:", self.salario_bruto)


class Gratificacao(Funcionario):

    def __init__(
        self,
        nome,
        cpf,
        salario,
        cargo: str,
        gratificacao: float
    ):
        super().__init__(nome, cpf, salario)

        self.cargo = cargo
        self.gratificacao = gratificacao

    def calcular_salario_anual(self):
        return (self.salario_bruto + self.gratificacao) * 12


def calcular_salario_anual(salario_bruto):
    return salario_bruto * 12


# FUNCIONÁRIO COMUM


print("-" * 30)
print("EXIBIR DADOS -> FUNCIONÁRIO COMUM")
print("-" * 30)

pessoa1 = Funcionario(
    "Joel Viana Sero",
    "12345678900",
    1621.00
)

pessoa1.exibir_dados()

anual = calcular_salario_anual(pessoa1.salario_bruto)

print(f"Funcionário: {pessoa1.nome}")
print(f"Salário bruto: R$ {pessoa1.salario_bruto:.2f}")
print(f"Salário Anual: R$ {anual:.2f}")


# FUNCIONÁRIO GERENTE

print("\n") 
print("-" * 30) 
print("EXIBIR DADOS -> GERENTE") 
print("-" * 30) 
pessoa2 = Gratificacao(
     "Maria Joana Viana da Silva", 
     "12345678230",
       7821.00, 
       "Gerente",
         1000.00 
        ) 

pessoa2.exibir_dados() 
print("Cargo:", pessoa2.cargo)
print("Gratificação: R$", pessoa2.gratificacao)

print("-" * 30) 
print("FOLHA DE PAGAMENTO") 
print("-" * 30) 
anual = pessoa2.calcular_salario_anual() 
print("Funcionário:", pessoa2.nome) 
print("Cargo:", pessoa2.cargo) 
print("Salário bruto: R$", pessoa2.salario_bruto) 
print("Gratificação: R$", pessoa2.gratificacao) 
print("Salário anual: R$", anual)

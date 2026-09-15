class Funcionario:

    def __init__(self, nome: str, cpf: str, salario: float):
        self.nome = nome
        self.cpf = cpf
        self.salario_bruto = salario
     


    def exibir_dados(self):
        print(self.nome)
        print(self.cpf)
        print(self.salario_bruto)

print("-"*30)
print("Exibir Dados-> Dados Brutos")

pessoa1 = Funcionario("Joel Viana Sero", "12345678900", 1621.00)
pessoa2 = Funcionario("Maria Joana Viana da Silva", "12345678230","Gerente", 7821.00)
pessoa1.exibir_dados()



def calcular_salario_anual(salario_bruto):
    return salario_bruto*12

print("-"*30)
print("Folha de Pagamento")
anual = calcular_salario_anual(pessoa1.salario_bruto)
print("Funcionário:",pessoa1.nome)
print("Salário bruto:", pessoa1.salario_bruto)
print("Salário Anual:R$ ",anual)


class Gratificacao(Funcionario):
    def __init__(self, nome, cpf, salario,cargo:str,gratificacao:float):
        super().__init__(nome, cpf, salario)    

        self.cargo = cargo
        self.gratificacao = gratificacao

    def calcular_salario_anual(self):
        return (self.salario_bruto + self.gratificacao) *12


print("Exibir Dados-> Dados Brutos")
pessoa2.exibir_dados()

print("-"*30)
print("Folha de Pagamento")
anual = calcular_salario_anual(pessoa1.salario_bruto)
print("Funcionário:",pessoa2.nome)
print("Salário bruto:", pessoa2.salario_bruto)
print("Salário Anual:R$ ",anual)

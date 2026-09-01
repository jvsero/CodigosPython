import math
num=int(input("Digite um número:  "))
raiz=math.sqrt(num)
print("---------- Informações ------------")
print(" Usando a Biblioteca math através do import math")
print("A raiz de {}  usando o math.sqrt é igual a {} ".format(num,raiz))
print("A raiz de {}  usando o math.sqrt  e o :.2f é igual a {:.2f} ".format(num,raiz))
print("A raiz de {}  usando o math.floor é igual a {} ".format(num,math.floor(raiz)))
print("A raiz de {}  usando o math.ceil é igual a {} ".format(num,math.ceil(raiz)))

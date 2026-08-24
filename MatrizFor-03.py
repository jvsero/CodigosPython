escada=[]

for i in range(1,6):
    linha=[]
    for j in range(i):
        linha.append("#")

    escada.append(linha)

    for linha in escada:
        print("".join(linha))






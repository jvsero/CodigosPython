rograma que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
'''

import random

alunos = ["Ana", "Bruno", "Carla", "Daniel","Joel","Amanda"]

print("Lista de Alunos Presentes:")

for aluno in alunos:
    print(aluno)


# Fazer 2 sorteios sem repetir
ultimos_sorteados = random.sample(alunos, 2)


print("-----------------------------")
print("     APAGAR O QUADRO 🟩")
print("\nÚltimos 2 alunos sorteados para apagar o 🟩:")

for aluno in ultimos_sorteados:
    print("🎁", aluno)
    

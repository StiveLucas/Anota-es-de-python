import os
os.system("cls || clear")

#Variáveis.
notas = []
QUANTIDADE_NOTAS = 3

#Dados do usuário.
for x in range(3):
    nota = float (input(f"Digite sua {x + 1}º nota: "))
    notas.append(nota)

# Calculo.
media = sum(notas) / QUANTIDADE_NOTAS

import os
os.system("cls || clear")
#Resultados
for x in range(1):
    print(f"Notas: {notas}")

print(f"Média: {media}")

import os
os.system("cls || clear")

#Variavel.
print("Digite quatro notas.")
soma = 0

for x in range(1, 5):
    notas = float (input("Digite sua {x}º: "))
    soma += notas

#Calculos.
media = soma / x

import os
os.system("cls || clear")
print("---Resultados---")
print(f"Média: {media}")
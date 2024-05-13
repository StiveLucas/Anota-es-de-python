import os
os.system("cls || clear")

#Variavel.
contaddorPar = 0
contadorImpar = 0

for x in range(1, 6):
  numero = int(input(f"Digite seu {x}º número: "))
if numero % 2 == 0:
    contaddorPar += 1
else:
    contadorImpar += 1

import os
os.system("cls || clear")
print("---Resultados---")
print(f"Quantidade de números pares: {contaddorPar}")
print(f"Quantidade de números ímpares: {contadorImpar}")
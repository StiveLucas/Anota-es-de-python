import os
os.system("cls || clear")

#Variáveis.
soma = 0

for x in range(1, 6):
    numero = int(input(f"Digite seu {x}º número: "))
    soma += numero

    print(f"Soma: {soma}")
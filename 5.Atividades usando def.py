import os
os.system("clear || cls")

numeros = []
x = 0

def cabecalho():
    print("------------------")
    print("===== Senai =====")
    print("------------------")

for x in range(5):
    x += 1
    numero = int (input(f"Digite o {x}º número: "))
    numeros.append(numero)

for x in range(5):
    x = 0
    x += 1
    print(f"{numeros}")
    cabecalho()
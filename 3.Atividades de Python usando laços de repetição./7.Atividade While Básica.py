import os
os.system("cls || clear")

#Variáveis.
notas: float = -1

while (notas < 0 or notas > 10):
    notas = float (input("Digite uma nota: "))

print(f"Nota informada: {notas}")
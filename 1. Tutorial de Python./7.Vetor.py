import os
os.system("cls || clear")

notas = []

for x in range(3):
    nota = float (input(f"Digite a {x + 1}º nota: "))
    notas.append(nota)  # O comando .append() serve para armazenar os vetores.0

x = 1

for x in range(3):
    print(f"{x}º nota: {notas}")


'''

comando para apresentar um por um.

palavras = ["carro", "barco", "avião"]
print(palavras)

for x in palavras:
    print(x)

'''
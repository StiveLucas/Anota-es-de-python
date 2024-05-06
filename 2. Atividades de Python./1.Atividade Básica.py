import os
os.system("cls || clear")

#Variáveis.
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
notaUm = float(input("Digite sua Primeiro nota: "))
notaDois = float(input("Digite sua Segunda nota: "))

somaDasNotas = notaUm + notaDois
media: float

#Calculo.
media = somaDasNotas / 2

#Resultados.
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {notaUm}")
print(f"Segunda nota: {notaDois}")
print(f"Média: {media}")
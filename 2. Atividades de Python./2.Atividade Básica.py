import os
os.system("cls || clear")

#Variáveis.
nomeAluno = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite sua 1º nota: "))
segundaNota = float(input("Digite sua 2º nota: "))
terceiraNota = float(input("Digite sua 3º nota: "))

#Calculo.
somaNotas = primeiraNota + segundaNota + terceiraNota
media = somaNotas / 3

import os
os.system("cls || clear")
#Resultado.
print(f"Nome: {nomeAluno}")
print(f"Idade: {idade}")
print(f"1º nota: {primeiraNota}")
print(f"2º nota: {segundaNota}")
print(f"3º nota: {terceiraNota}")
print(f"Média: {media}")

if media >= 7:
    print(f"Aprovado")
else:
    print(f"Reprovado")
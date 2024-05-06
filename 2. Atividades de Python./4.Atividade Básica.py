import os
os.system("cls || clear")

#Variáveis.
primeiroNumero = float(input("Digite seu Primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))

maior = max(primeiroNumero, segundoNumero)
menor = min(primeiroNumero, segundoNumero)

#Calculos.
soma = primeiroNumero + segundoNumero
multi = primeiroNumero * segundoNumero
media = soma / 2

import os
os.system("cls || clear")

#Resultado.
print("---Resultados---")
print(f"Soma: {soma}")
print(f"Multiplicação: {multi}")
print(f"Média: {media}")
print(f"------------")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
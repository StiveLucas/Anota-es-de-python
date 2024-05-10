import os 
os.system("cls || clear")

#Variáveis.
nomeDoProduto = str(input("Digite o nome do produto: "))
quantidadeDoProduto = int(input("Digite a quantidade do produto: "))
precoUnitario = float(input("Digite sua o Preço Unitário: R$"))

#Calculos
total: float = quantidadeDoProduto * precoUnitario
if quantidadeDoProduto <= 5:
    desconto: float = (2 * total) / 100
    quantidadeDeDesconto: int = 2

if quantidadeDoProduto > 5 and quantidadeDoProduto <= 10:
    desconto: float = (3 * total) / 100

if quantidadeDoProduto > 10:
    desconto: float = (5 * total) / 100

valorComDesconto: float = total - desconto

import os 
os.system("cls || clear")
#Resultado
print("---Resultados---")
print(f"Nome do produto: {nomeDoProduto}")
print(f"Total do a pagar: R${total}")
print(f"------------------------------")
print(f"Desconto de {quantidadeDeDesconto}%")
print(f"Total a pagar com desconto: R${valorComDesconto}")
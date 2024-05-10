import os 
os.system("cls || clear")

#Variáveis.
print("Digite os 2 números e a operação desejada.")
print("Digite:")
print(" (+) soma \n (-) Subtração \n (*)Multiplicação \n (/) Divisão \n")

primeiroNumero = int (input("Digite o 1º número: "))
segundoNumero = int (input("Digite seu 2º número: "))
operacao = str (input("Digite a operação: "))

#Calculo.
soma: float = primeiroNumero + segundoNumero
subtracao: float = primeiroNumero - segundoNumero
multiplicacao: float = primeiroNumero * segundoNumero
divisao: float = primeiroNumero / segundoNumero

import os 
os.system("cls || clear")
#Resultado
print("---Resultado---")
match(operacao):
    case '+':
        print(f"Soma: {soma}")
    case '-':
        print(f"Subtração: {subtracao}")
    case '*': 
        print(f"Multiplicação: {multiplicacao}")
    case '/':
        print(f"Divisão: {divisao}")
    case _:
        print("Opção inválida.")

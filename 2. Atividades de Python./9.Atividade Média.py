import os 
os.system("cls || clear")

#varáveis
nome = str(input("Digite seu nome: "))
sexo = str (input("Digite seu sexo (F ou M): "))
sexo = sexo.upper()

if sexo != 'F' and sexo != 'M':
    print("Opção inválida.")

estadoCivil = str (input("Digite seu estado civil: "))
estadoCivil = estadoCivil.upper()

if sexo == 'F' and estadoCivil == "CASADA":
    tempoDeCasada = int (input("Digite seu tempo de casada: "))

import os 
os.system("cls || clear")
#Resultado.
print("---Resultado---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estadoCivil}")

if sexo == 'F' and estadoCivil == "CASADA":
 print(f"Tempo de casada: {tempoDeCasada}")
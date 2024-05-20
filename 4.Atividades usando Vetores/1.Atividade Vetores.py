import os
os.system("cls || clear")

#Variavel.
valores = []
quantidadeDePares = 0
quantidadeDeImpares = 0 

#Dados do usuário.
for x in range(6):
    valor = int (input(f"Digite sua {x + 1}º nota: "))

    if valor % 2 == 0:
        quantidadeDePares += 1
    
    else:
        quantidadeDeImpares += 1

    valores.append(valor)

import os
os.system("cls || clear")
#Resultado
print("---Resultados---")    
for x in range(1):
    print(f"Quantidade de números:")
    print(f"Pares: {quantidadeDePares}")
    print(f"Ímpares: {quantidadeDeImpares}")
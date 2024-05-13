import os
os.system("cls || clear")

#Variáveis.
notas: float = -1
soma: float = 0

#Dados do usuário
for x in range(1, 3):
    while True:
        notas = float(input(f"Digite sua {x}º nota: "))

        if notas > 10 or notas < 0:
            print("Nota inválida")
        else:
            soma += notas
            break     

#Calculo.
media : float = soma / x

import os
os.system("cls || clear")
#Resultados.
print("---Resultados---")
print(f"Média: {media}")
import os
os.system("cls || clear")

#variáveis.
notaUm: float = -1
notaDois: float = -1

while(notaUm > 10 or notaDois < 0):
    notaUm = float (input(f"Digite sua 1º nota: "))
    notaDois = float (input(f"Digite sua 2º nota: "))

#Calculo.
media: float = (notaUm + notaDois) / 2

import os
os.system("cls || clear")
#Resultados
print("---Resultados---")
print(f"1º Nota: {notaUm}")
print(f"2º Nota: {notaDois}")
print(f"Média: {media}")

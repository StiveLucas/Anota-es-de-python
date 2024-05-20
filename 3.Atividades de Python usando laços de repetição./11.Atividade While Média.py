import os
os.system("cls || clear")
import time

#Atribuindo valores.
x = 1
contador_Notas: int = 0
soma_Notas = 0

#Menu
while True:
    print("=== Menu ===")
    print("Comando |  Descrição")
    print("S | Inserir uma nota.")
    print("P | Ver quantas notas foram inseridas.")
    print("N | Calcular a média das notas.")
    comando = str (input(f"Digite seu comando: "))
    comando = comando.upper()

    print("\n")
 #Dados do usuário.
    if comando == 'S':
        import os
        os.system("cls || clear")
        
        nota = float (input(f"Digite sua {x}º nota: "))
        x += 1
        contador_Notas += 1
        soma_Notas += nota

    elif comando == 'P':
        print("---Resultados---")
        print(f"quantidade de notas inseridas: {contador_Notas}")
    
    elif comando == 'N':
        print("---Resultados---")
        media = soma_Notas / contador_Notas
        print(f"Média das notas: {media}")
        break
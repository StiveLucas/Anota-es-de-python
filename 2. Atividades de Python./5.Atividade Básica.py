import os
os.system("cls || clear")

#Variáveis.
login: str = "luccas22"
senha: str = "126"


#Dados do usuário.
login = str(input("Digite seu login: "))
senha = str(input("Digite sua senha: "))

#Resultados
print("---Resultados---")
if login == "luccas22" and senha == "126" :
    print("Bem Vindo")
else:
    print("Login inválida.")
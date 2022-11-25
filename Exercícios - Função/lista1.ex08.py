#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def letra(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        print("A letra é uma vogal")
    else:
        print("A letra é uma consoante")

x = str(input("Digite uma letra:"))

letra(x)
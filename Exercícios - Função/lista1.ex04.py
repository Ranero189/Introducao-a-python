#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a,b,c):
    resultado = a + b + c
    print("A soma é:", resultado)

x = int(input("Digite um numero:"))
y = int(input("Digite um numero:"))
z = int(input("Digite um numero:"))

soma(x,y,z)
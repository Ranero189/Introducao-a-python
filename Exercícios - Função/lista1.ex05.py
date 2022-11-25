#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo

def numero(a):
    if a > 0:
        print("P")
    elif a <= 0:
        print("N")

x = int(input("Digite um numero:"))

numero(x)
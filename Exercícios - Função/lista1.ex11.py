#Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

def triangulo(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        print("Os segmentos acima PODEM FORMAR um triangulo", end=' ')
        if a == b == c:
            print("EQUILÁTERO")
        elif a != b and a != c:
            print("ESCALENO")
        else:
            print("ISÓSCELES")
    else:
        print("Os segmentos acima NÃO PODEM FORMAR um triangulo")

r1 = float(input("Primeiro segmento:"))
r2 = float(input("Segundo segmento:"))
r3 = float(input("Terceiro segmento:"))

triangulo(r1,r2,r3)
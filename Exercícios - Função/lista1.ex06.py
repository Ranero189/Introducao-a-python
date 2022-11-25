#Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A= (base x altura) / 2).

def area(a,b):
    resultado = (a*b)/2
    print("A area do triangulo é:", resultado)

x = float(input("Digite a altura:"))
y = float(input("Digite o tamanho da base:"))

area(x,y)
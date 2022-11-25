def somar(a, b):
#a e b são parametros da função somar

    resultado = a + b
    print("A soma é:", resultado)

def dividir(a, b):
    resultado = a/b
    print("A divisão é:", resultado)

#x e y são argumentos que serão passados para a função
x = float(input("Digite um numero: "))
y = float(input("Digite um numero: "))

somar(x, y)
dividir(x, y)
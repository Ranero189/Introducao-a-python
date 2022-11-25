def somar(a, b):
    return a + b

def dividir(a , b):
    resultado = a/b
    print("O resultado é:", resultado)

x = float(input("Digite um numero: "))
y = float(input("Digite um numero: "))
w = somar(x , y)

print(f"O valor de w é: {w}")
print(somar(x, y))
dividir(x , y)
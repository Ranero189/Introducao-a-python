import math

angulo = int(input("Informe o angulo: "))

dist = int(input("Informe a distancia: "))

tg = math.tan(angulo)

altura = math.floor(tg * dist)

print(f"A altura do predio é {altura}")
from random import randint

vet = []

valores = []

repetidos = set()

for i in range(10):
    vet.append(randint(1, 10))

print(vet)

for vet in vet:

    if vet not in valores:
        valores.append(vet)

    else:
        repetidos.add(vet)

print(f"Valores = {valores}")

print(f"Repetidos = {repetidos}")

print(f"A quantidade de elementos repetidos é:", len(repetidos))
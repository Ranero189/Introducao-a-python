vet = []

vet1 = []

for i in range(30):
    vet.append(int(input(f"Digite um valor para a posição {i} do vetor")))

print(vet)

for i in range(30):

    if vet[i] > 0:
        vet1.append(1)

    else:
        vet1.append(0)

print(vet1)
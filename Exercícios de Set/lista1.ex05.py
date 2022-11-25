vet = []

for i in range(5):
    vet.append(int(input(f"Digite um valor para a posição {i} do vetor")))

set = set(vet)

print(vet)

print(set)

print(f"A quantidade de elementos únicos é:", len(set))
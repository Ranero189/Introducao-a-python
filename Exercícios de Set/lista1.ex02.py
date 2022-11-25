mat1 = [[0 for i in range(3)]for j in range(3)]

vet = []

for i in range(3):
    for j in range(3):
        mat1[i][j] = input(f"Digite um valor para a posição {i} {j} da matrix")

        if i == j:
            vet.append(mat1[i][j])

for i in range(3):
    for j in range(3):
        print(f"[{mat1[i][j]:^5}]", end =" ")
    print()

print(vet)
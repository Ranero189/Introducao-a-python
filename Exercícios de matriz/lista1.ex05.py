mat1 = [[0 for j in range(4)] for i in range(4)]

soma = 0

for i in range (4):
    for j in range (4):

        mat1[i][j] = int(input("Digite um numero: "))

        if i == j:
            soma += mat1[i][j]

for i in range (4):
    for j in range (4):
        print(f'[{mat1[i][j]:^5}]', end=" ")
    print()

print("A soma é:", soma)
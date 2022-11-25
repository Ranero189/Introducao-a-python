mat1 = [[0 for j in range(3)] for i in range(3)]

for i in range (3):
    for j in range (3):

        mat1[i][j] = int(input("Digite um numero: "))

for i in range (3):
    for j in range (3):
        print(f'[{mat1[i][j]:^5}]', end=" ")
    print()

print()

for i in range (3):
    for j in range (3):
        print(f'[{mat1[j][i]:^5}]', end=" ")
    print()
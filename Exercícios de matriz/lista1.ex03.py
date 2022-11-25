mat1 = [[" " for j in range(3)] for i in range(3)]

for i in range (3):
    for j in range (3):
        mat1[i][j] = str(input("Digite um nome: "))

for i in range (3):
    for j in range (3):
        print(f'[{mat1[i][j]:^5}]', end=" ")
    print()
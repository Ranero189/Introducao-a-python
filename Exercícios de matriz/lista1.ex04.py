mat1 = [[" " for j in range(2)] for i in range(5)]

for i in range (5):
    for j in range (2):

        if j == 1:
            mat1[i][j] = input("Digite o nome do anuno: ")

        else:
            mat1[i][j] = input("Digite a idade do anuno: ")

for i in range (5):
    for j in range (2):
        print(f'[{mat1[i][j]:^5}]', end=" ")
    print()
mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range (3):
    for i in range (3):
        mat[l][i] = int(input(f'digite um valor: '))

for l in range(3):
    for i in range(3):
        print(f'[{mat[l][i]:^5}]', end=" ")
    print()
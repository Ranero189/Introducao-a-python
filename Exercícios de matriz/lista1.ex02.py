from random import randint

mat1 = [[0 for j in range(3)] for i in range(3)]

mat2 = [[0 for j in range(3)] for i in range(3)]

mat3 = [[0 for j in range(3)] for i in range(3)]

mat4 = [[0 for j in range(3)] for i in range(3)]

for i in range (3):
    for j in range (3):

        mat1[i][j] = int(input("Digite um numero: "))
        mat2[i][j] = randint(1, 100)
        mat3[i][j] = mat1[i][j] + mat2[i][j]
        mat4[i][j] = mat2[i][j] * mat1[i][j]

for i in range (3):
    for j in range (3):
        print(f'[{mat1[i][j]:^5}]', end=" ")
    print()

print()

for i in range (3):
    for j in range (3):
        print(f'[{mat2[i][j]:^5}]', end=" ")
    print()

print()

for i in range (3):
    for j in range (3):
        print(f'[{mat3[i][j]:^5}]', end=" ")
    print()

print()

for i in range (3):
    for j in range (3):
        print(f'[{mat4[i][j]:^5}]', end=" ")
    print()
#Crie um programa que calcule e mostre a média aritmética dos números pares entre 10 e 50

soma = 0
cont = 0

for c in range(10, 52, 2):
    if c % 2 == 0:
        cont += 1
        soma += c

print(f'A media dos {cont} valores solicitados é: {soma/cont}')
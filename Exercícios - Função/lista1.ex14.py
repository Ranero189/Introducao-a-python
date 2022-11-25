#Faça um programa que leia 5 números e informe o maior número.

maior = -999999999999

for i in range(0, 5):
    x =int(input("Digite um numero:"))
    if x > maior:
        maior = x

print("O maior numero digitado é:", maior)
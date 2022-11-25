#Escreva um programa que leia 15 valores reais, encontra o maior e o menor deles e mostra o resultado.

maior = -9999999
menor = 9999999

for c in range(15):
    x = int(input('Digite 15 numeros: '))
    if x > maior:
     maior = x
    if x < menor:
     menor = x
     
print(menor, maior)
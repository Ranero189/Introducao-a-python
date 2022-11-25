#Faça um programa que receba 20 números inteiros e mostre o maior par e o menor ímpar dentre todos os números.​

maior = -9999999
menor = 9999999
maior_par = 0
menor_impar = 0

for c in range(20):
    x = int(input('Digite 20 numeros: '))
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    if maior % 2 == 0:
        maior_par= maior
    if menor % 2 != 0:
        menor_impar = menor

print('-'*60)
print('O maior numero par é {} e o menor impar é {}'.format(maior_par, menor_impar))
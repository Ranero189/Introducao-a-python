#Faça um programa que leia vários inteiros positivos e mostre, no final, a soma dos números pares e a soma dos números ímpares.
#O programa para quando entrar um número maior que 1000.

par = 0
impar = 0
c = 0

for c in range(5):
    n = int(input('Digite 5 numeros =< que 1000: '))
    if n > 1000:
        print('-'*40)
        print('Valor inserido é invalido')
        break
    if n % 2 == 0:
        par += n
    if n % 2 != 0:
        impar += n
    if c == 4:
        print('-'*40)
        print('A soma dos numeros pares é {} e a soma dos numeros impares é {}'.format(par, impar))
#Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. ​

soma = 0
N = int(input('Digite um numero: '))
print('-='*20)
print('Os divisores de', N ,'são: ')
print('-'*30)
for i in range(1, N):
    if N % i == 0:
        soma += i
        print('{}'.format(i), end=' ')

print(end='\n')
print('-'*30)
print('A soma dos divisores é {}'.format(soma))
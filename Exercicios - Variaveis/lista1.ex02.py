#Crie um programa que leia 4 números reais do teclado e imprima a média entre eles.

n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))
n4 = int(input('Insira o quarto numero: '))
média = (n1 + n2 + n3 + n4)/4

print('A média entre {}, {}, {} e {} é {}'.format(n1, n2, n3, n4, média))

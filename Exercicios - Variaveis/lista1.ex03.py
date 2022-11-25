#Faça um programa que leia 2 números reais e calcule e mostre a soma,a multiplicação,a subtração,a divisão,o resto da divisão,a potenciação e a média entre eles.

altura = float(input('Insira a altura: '))
comprimento = float(input('Insira o comprimento da base: '))

triangulo = (altura*comprimento)/2
quadrado = comprimento**2

print('Se for um quadrado, a área será {} e se for um triangulo, será {}'.format(quadrado, triangulo))
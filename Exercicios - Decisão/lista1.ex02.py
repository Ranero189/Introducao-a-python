#Faça um programa que leia dois inteiros A e B e imprima a soma destes valores se eles forem iguais.
#senão, ou seja, se forem diferentes imprima o seu produto.

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
if a == b:
  print("A soma desses numeros é:", a+b)
else:
  print("O produto desses numeros é:", a*b)
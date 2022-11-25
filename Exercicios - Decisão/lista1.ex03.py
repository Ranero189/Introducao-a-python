#Faça um programa que leia dois números A e B e imprima o maior deles.
#Caso estes números sejam iguais, imprima “Iguais.”​

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
if a > b:
  print("O maior numero é:", a)
elif a == b:
  print("Os numeros são iguais")
else:
  print("O maior numero é:", b)
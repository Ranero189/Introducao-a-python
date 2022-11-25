#Faça um programa que leia 3 números inteiros e imprima o menor deles. ​

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite outro numero: "))
if a < b and c:
  print("O menor numero é:", a)
elif b < a and c:
  print("O menor numero é:", b)
elif c < b and a:
  print("O menor numero é:", c)
#Faça um programa que leia os valores A, B, C e diga se a soma de A + B é menor ou maior que C. ​

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite outro numero: "))
if a+b > c:
  print("A soma de {} + {} é maior do que {}".format(a, b, c))
else:
  print("A soma de {} + {} é menor do que {}".format(a, b, c))
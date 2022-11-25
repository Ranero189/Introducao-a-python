#Faça um programa que leia dois números inteiros A e B e retorne o quociente da divisão entre A e B.
#O programa deve verificar, previamente à divisão, se o valor de B é diferente de zero. ​

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
if b > 0:
  print("O quoeficiente da divisão é:", (a/b))
#Seja três valores reais e distintos, A, B e C. 
#Fazer um programa que leia estes valores (que formam os coeficientes de uma equação de 2º. Grau). 
#Verificar e calcular as raízes da equação, quando existirem. ​

a = float(input("Digite um numero: "))
b = float(input("Digite outro numero: "))
c = float(input("Digite outro numero: "))
if a == b and b == c and a == c:
  print("Digite numeros distintos")
elif a and b and c > 0:
 d = (b**2 - 4*a*c)
 x1 = (-b + d**(1/2))/(2*a)
 x2 = (-b - d**(1/2))/(2*a) 
 print("O valor de x1 é: {:.1f}".format(x1))
 print("O valor de x2 é: {:.1f}".format(x2))
else:
  print("A equação é incompleta")
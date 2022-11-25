#Faça um programa que leia dois valores A e B. 
#Se os valores forem iguais deverá ser calculada a raiz quadrada  dos dois valores.
#caso contrário elevar A por B e armazenar o resultado em uma variável C. 

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
if a == b:
  print("A raiz quadrada de {} e {} é:".format(a, b), a**0.5)
else:
  c = a**b
  print("{} elevado por {} é: {}".format(a, b, c))
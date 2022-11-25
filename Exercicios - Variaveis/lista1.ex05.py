#Faça um programa que leia seu nome completo,seu curso e seu RA,e mostre os resultados e os tipos de cada variável utilizada.

nome = str(input('Qual é seu nome? '))
ra = str(input('Qual é seu RA? '))
curso = str(input('Qual é seu curso? '))

print('Olá {}'.format(nome))
print(type(nome))

print('Seu RA é {}'.format(ra))
print(type(ra))

print('Você está cursando {}'.format(curso))
print(type(curso))
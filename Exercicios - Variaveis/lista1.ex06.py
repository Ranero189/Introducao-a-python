#Faça um programa que leia seu nome completo e mostre seu nome com todas as letras minúsculas,todas as letras maiúsculas e só a primeira letra maiúscula.

nome = str(input('Insira seu nome: '))

print('Seu nome é {}'.format(nome.lower()))
print(' ')
print('Seu nome é {}'.format(nome.upper()))
print(' ')
print('Seu nome é {}'.format(nome.capitalize()))

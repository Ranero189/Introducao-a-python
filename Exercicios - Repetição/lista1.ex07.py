#Receber um nome e imprimir as letras na posição impar

nome = str(input('Digite um nome: '))
print('-'*40)
print('Os caracteres nos índices pares são:', nome[::2])
print('Os caracteres nos índices ímpares são:', nome[1::2])
#Receber do teclado um nome e imprimir tantas vezes quantos forem seus caracteres.

nome = str(input('Digite um nome: '))
n = len(nome)
print('-'*30)
for c in range(n):
    print(nome)
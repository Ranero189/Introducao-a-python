#Estrutura o for - loop
# escrevendo a tabuada

tabuada=int(input("Digite um numero: "))

for numero in range(1, 11, 1):
    print(numero,'X', tabuada,'=', numero * tabuada)
#Fazer um algoritmo para escrever a soma dos​ números múltiplos de 7 entre 100 e 200.​

soma = 0
cont = 0

for c in range(100, 201):
    if c % 7 == 0:
        cont += 1
        soma += c

print(f'A soma dos {cont} valores solicitados é: {soma}')
import random

vet1 = []

vet2 = []

num = int(input("Imforme o tamanho dos vetores"))

for i in range(num):
    vet1.append(int(input("Digite um numero:")))
    vet2.append(int(random.randint(1,10)))

iguais = (set(vet1) & set(vet2))

print("vetor1 ", vet1)

print("vetor2 ", vet2)

print("conjunto ", iguais)
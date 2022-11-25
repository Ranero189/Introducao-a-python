import random

vet1 = []

def vetor(a):

    for i in range(a):
        vet1.append(int(random.randint(1,100)))

num = int(input("Informe o tamanho do vetor:"))

vetor(num)
print(vet1)
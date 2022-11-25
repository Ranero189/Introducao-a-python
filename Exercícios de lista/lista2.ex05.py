import random

vet1 =[]

vet2 =[]

vet3 =[]

for i in range(5):
    vet1.append(random.randint(1,100))
    vet2.append(random.randint(1,100))

for i in range(5):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print(vet1)

print('')

print(vet2)

print('')

print(vet3)
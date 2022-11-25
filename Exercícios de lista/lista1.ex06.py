import random 

vet1 = [] 

for i in range(10): 
    num = random.randint(1,100) 
    vet1.append(num) 
    if vet1[i] % 2 == 0: 
        print(f'O valor Par {vet1[i]} esta na posição {i}') 
    else: print(f'O valor Impar {vet1[i]} esta na posição {i}')
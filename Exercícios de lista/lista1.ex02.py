vet1 = [] 

for i in range(9): 
    print("Digite um valor para a posição", i,"do vetor:") 
    vet1.append(int(input())) 

vet1.sort() 
print(vet1) 
print(max(vet1))
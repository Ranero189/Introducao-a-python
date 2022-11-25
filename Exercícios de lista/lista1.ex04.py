vet1 = []
 
vet2 = [] 

x = int(input("Digite um numero:")) 

for i in range(5): 
    print("Digite um valor para a posição", i,"do vetor:") 
    vet1.append(int(input())) 

for i in range(5): 
    vet2.append(vet1[i] * x) 
    
print(vet2)
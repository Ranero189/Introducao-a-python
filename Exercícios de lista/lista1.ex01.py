vet1 = [] 

for i in range(3): 
    print("Digite um valor para a posição", i,"do vetor x:") 
    vet1.append(float(input()))

vet2 = [] 

for i in range(3): 
    print("Digite um valor para a posição", i,"do vetor y:") 
    vet2.append(float(input())) 

resp = []

for i in range(3): 
    resp.append(vet1[i]+vet2[i]) 
print("O vetor resultante é:", resp)
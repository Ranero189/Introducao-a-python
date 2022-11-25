notas = [] 

for i in range(5): 
    notas.append(input("Digite seus nomes: ")) 
    notas.insert(0, float(input("Digite sua nota: "))) 

for i in range(5): 
    print(notas[i], " ", notas[i+5])
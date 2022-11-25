from random import randint 

lancamentos = [] 

f1 = 0 
f2 = 0
f3 = 0 
f4 = 0 
f5 = 0 
f6 = 0 

for i in range(50): 
    random = (randint(1 , 6)) 
    lancamentos.append(str(random)) 
    if random == 1: 
        f1 += 1 
    elif random == 2: 
        f2 += 1 
    elif random == 3: 
        f3 += 1 
    elif random == 4: 
        f4 += 1 
    elif random == 5: 
        f5 += 1 
    elif random == 6: 
        f6 += 1

print(f'A porcentagem de 1 é {(f1*100)/50}%') 
print(f'A porcentagem de 2 é {(f2*100)/50}%') 
print(f'A porcentagem de 3 é {(f3*100)/50}%') 
print(f'A porcentagem de 4 é {(f4*100)/50}%') 
print(f'A porcentagem de 5 é {(f5*100)/50}%') 
print(f'A porcentagem de 6 é {(f6*100)/50}%')
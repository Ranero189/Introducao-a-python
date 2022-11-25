#Faça um programa que calcule o S, sendo:​ S = 1-(2/4)+(3/9)-(4/16)+(5/25)-(6/36)...(-10/100)

s = 0
for i in (1, -10/100):
    if i % 2 != 0:
        s = s + (i / (i * i)) 
    else:
        s = s - (i / (i * i)) 

print(s)
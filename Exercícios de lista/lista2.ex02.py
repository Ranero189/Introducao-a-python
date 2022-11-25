import random

def bin(a):

    num = ""
    for i in range(a):
        temp = str(random.randint(0, 1))
        num += temp

    return(num)

n = random.randint(1, 64)

bin(n)

binario = int(bin(n))
valor = binario

decimal = 0
i = 0

while n >= 0:
    
    resto = binario % 10
    decimal = decimal + (resto * (2**i))
    n = n - 1
    i = i + 1

    binario = binario // 10

print("(Binario) ",valor,"(Decimal) ",decimal)
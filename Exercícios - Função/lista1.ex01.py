#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

def gorjeta(total):
    resultado = conta * (10/100)
    print ("A gorjeta do garçom é: R$", resultado)

conta = float(input("Informe o valor da conta:"))
gorjeta(conta)
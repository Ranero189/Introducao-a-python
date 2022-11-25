#Faça uma função que dado um numero inteiro, imprima o numero de linhas correspondente ao numero do momento até o numero digitado.​
#1​
#22​
#333​
#......​
#nnnnnnn

def repetição(a):
      for linha in range(num+1):
            for m in range(linha):
                  print(linha, end=" ")
            print(end="\n")       

num = int(input("Digite um numero inteiro: "))

repetição(num)
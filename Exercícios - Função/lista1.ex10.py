#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 

def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sabado"
        case _:
            return "Valor {} invalido".format(dia)

x = int(input("Digite o o dia da semana, respectivamente (1 = domingo, 2 = segunda, ...)"))

print(dia_semana(x))
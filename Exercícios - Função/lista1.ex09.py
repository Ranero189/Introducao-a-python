#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR: ​
#Salário Bruto até 900 (inclusive) - isento ​
#Salário Bruto até 1500 (inclusive) - desconto de 5% ​
#Salário Bruto até 2500 (inclusive) - desconto de 10% ​
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.​
#No exemplo o valor da hora é R$ 5,00 e a quantidade de hora é 220.​

def salario(a, b):
    salario_bruto = a*b
    print("Seu salario bruto é:", salario_bruto)
    if salario_bruto <= 900:
        salario_liquido = salario_bruto
    elif salario_bruto <= 1500:
        salario_liquido = salario_bruto - (salario_bruto*(5/100))
    elif salario_bruto <= 2500:
        salario_liquido = salario_bruto - (salario_bruto*(10/100))
    elif salario_bruto > 2500:
        salario_liquido = salario_bruto - (salario_bruto*(20/100))
    print("Seu salario liquido é:", salario_liquido)

x = float(input("Informe o valor por hora:"))
y = float(input("Informe o numero de horas trabalhadas por mês:"))

salario(x,y)
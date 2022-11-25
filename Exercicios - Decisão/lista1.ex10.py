#Uma empresa decidiu conceder um aumento de salários a seus funcionários.
#Fazer um programa que leia, para cada funcionário, o seu número e o seu salário atual.
#E escreve o número do funcionário, seu salário atual, o percentual de seu aumento e o valor do salário corrigido.
 
nI = str(input("Informe seu numero de identificação: "))
salario = float(input("Informe seu salario atual: "))
if salario <= 400:
  print("Olá {}, seu salario atual é {}, sofreu um almento de 15%, valor do salário corrigido:".format(nI, salario), salario+(salario*0.15))
elif salario > 400 and salario <= 700:
  print("Olá {}, seu salario atual é {}, sofreu um almento de 12%, valor do salário corrigido:".format(nI, salario), salario+(salario*0.12))
elif salario > 700 and salario <= 1000:
  print("Olá {}, seu salario atual é {}, sofreu um almento de 10%, valor do salário corrigido:".format(nI, salario), salario+(salario*0.10))
elif salario > 1000 and salario <= 1800:
  print("Olá {}, seu salario atual é {}, sofreu um almento de 7%, valor do salário corrigido:".format(nI, salario), salario+(salario*0.07))
elif salario > 1800 and salario <= 2500:
  print("Olá {}, seu salario atual é {}, sofreu um almento de 4%, valor do salário corrigido:".format(nI, salario), salario+(salario*0.04))
elif salario > 2500:
  print("Olá {}, seu salario atual é {}, não sofreu aumento".format(nI, salario))
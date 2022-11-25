#A Organização Mundial de Saúde (OMS) classifica as pessoas pela sua faixa etária, de acordo com a tabela a seguir.
#Leia o nome e a idade de uma pessoa e mostre sua classificação. ​

nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
if idade <= 12:
  print("Olá {}, sua classificação é (criança)".format(nome))
elif idade > 12 and idade <= 18:
  print("Olá {}, sua classificação é (adolescente)".format(nome))
elif idade > 18 and idade <= 59:
  print("Olá {}, sua classificação é (adulto)".format(nome))
elif idade >= 60:
  print("Olá {}, sua classificação é (idoso)".format(nome))
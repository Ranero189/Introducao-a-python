#Faça um programa que leia o nome e a três notas de uma disciplina de um aluno.
#ao final escreva o nome do aluno, sua média e se ele foi aprovado. 
#A média mínima para aprovação é 7​.

aluno = str(input("Digite seu nome: "))
n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))
n3 = int(input("Digite sua terceira nota: "))
media = (n1+n2+n3)/2
if media >= 7:
  print("Parabéns {}, você foi aprovado!".format(aluno))
else:
  print("Ops {}, você foi reprovado!".format(aluno))
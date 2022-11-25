#Faça um programa para controlar a secretaria da escola, a funcionária deve digitar o código e as notas de P1, T1, P2 e T2. 
#Calcule a média ponderada, onde as provas tem valor 0,7(0,35 cada) e os trabalhos 0,3(0,15 cada). 
#Será considerado aprovado quem tiver média acima de 6. 
#O programa deve permitir entradas dos códigos e das notas dos alunos até que a secretária digite o valor 0(zero).

while True:
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('nota 2: '))
    trabalho1 = float(input('Trabalho 1: '))
    trabalho2 = float(input('Trabalho 2: '))
    media = (nota1*(35/100)) + (nota2*(35/100)) + (trabalho1*(15/100)) + (trabalho2*(15/100))/(85/100)
    print('-='*30)
    print('A media do aluno é {:.1f}'.format(media))
    if media >= 7:
        print('--'*30)
        print('Aluno Aprovado!')
    elif media < 7:
        print('--'*30)
        print('Aluno reprovado!')
    resp = str(input('Quer continuar? (0 Interrompe) '))
    if resp in '0':
        break
print('Programa encerrado!')
print('<<< Volte sempre >>>')
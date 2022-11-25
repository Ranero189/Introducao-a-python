#Faça um programa que leia o seu ano de ingresso no curso, a duração do curso e calcule o ano de sua formatura e dê os parabéns.

ano_de_ingresso = int(input('Em qual ano você ingressou no curso?'))
duração_do_curso = int(input('Qual é a duração do curso? '))
ano_de_conclusão = duração_do_curso + ano_de_ingresso

print('Você ira se formar em {}, Parabéns!'.format(ano_de_conclusão))

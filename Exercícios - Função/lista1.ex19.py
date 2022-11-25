#Faça um programa que imprima todos os ângulos e senos desses ângulos de zero a 180.

from math import radians, sin, cos, tan
print('')
print('Ciclo do SENO de "0" à "180°"')
print('-='*18)
print('')
for angulo in range(0,181):
    seno = sin(radians(angulo))
    print("O angulo de {}° tem o SENO de {:.4f}".format(angulo, seno))
    print('')
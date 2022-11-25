#Escreva um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura em Fahrenheit.

C = float(input('Informe a temperatura em °C: '))
F = ((9*C)/5)+32

print('A temperatura de {}°C corresponde a {}°F!'.format(C, F))
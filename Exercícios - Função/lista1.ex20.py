#Sabendo que as linguagens de programação tema função seno em radianos, com base no exercício 13, converta os senos para graus​.

from math import sin, radians
print('')
print('SENO para GRAUS de "0" à "180°"')
print('-='*18)
print('')
for i in range(0, 181):
    if 0 <= i < 180:
        print(f'{sin(radians(i)):.4f} = {f"{i}°"}')
    else:
        print(f'{f"0.0000 = {i}°"}')
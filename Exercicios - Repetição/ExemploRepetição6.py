# tabuada 2.0v

while True:
    n = int(input('Quer ver a tabuada de qual numero? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
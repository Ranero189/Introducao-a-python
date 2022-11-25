#Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25. Imprimir o nome da pessoa e a palavra ACEITA. Caso contrário imprimir NAO ACEITA.​

nome = str(input('Nome: '))
idade = int(input('Idade: '))
Sexo = str(input('Sexo [M/F]: '))

if Sexo in 'Ff':
    if idade < 25:
        print(nome, 'Aceita')
    elif idade > 25:
        print(nome, 'Não aceita')
else:
    print(nome, 'Não aceita')
total = 0

media = 0

MelhorTempo = 999999999999999999999999

MelhorVolta = 0

NumeroVoltas = int(input("Digite o número de voltas: "))

tempo = []

for i in range(NumeroVoltas):

    print("Digite o tempo da ",i+1,"ª volta (em segundos): ")

    tempo.append(int(input()))

    total += tempo[i]

for i in range(NumeroVoltas):

    if tempo[i] < MelhorTempo:

        MelhorTempo = tempo[i]

        MelhorVolta = i+1

media = total/NumeroVoltas

print("O melhor tempo foi: ", MelhorTempo, " segundos.")

print("Melhor volta foi a ", MelhorVolta,"ª.")

print(f"A média de tempo foi: {media:.1f}")
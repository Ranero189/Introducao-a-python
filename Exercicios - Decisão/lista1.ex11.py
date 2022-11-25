#A OMS estipula faixas de IMC para decidir se a pessoa está com peso normal, ou abaixo do peso, ou acima do peso.
#Para saber qual é a sua situação, depois de calcular IMC, você deve encontrar o seu índice na seguinte tabela.
#A formula de cálculo do IMC em geral é: IMC= peso / altura2.

altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))
imc = imc = peso / altura**2
if imc < 15:
  print("seu imc é {:.1f}, cuidado! você está Extremamente abaixo do peso​".format(imc))
elif imc >= 15 and imc <= 16:
  print("seu imc é {:.1f}, cuidado! você está Gravemente abaixo do peso​".format(imc))
elif imc >= 16 and imc <= 18.5:
  print("seu imc é {:.1f}, cuidado! você está Abaixo do peso ideal​".format(imc))
elif imc >= 18.5 and imc <= 25:
  print("seu imc é {:.1f}, Parabéns! você está na Faixa de peso ideal".format(imc))
elif imc >= 25 and imc <= 30:
  print("seu imc é {:.1f}, cuidado! você está com Sobrepeso​".format(imc))
elif imc >= 30 and imc <= 35:
  print("seu imc é {:.1f}, cuidado! você está com Obesidade grau I".format(imc))
elif imc >= 35 and imc <= 40:
  print("seu imc é {:.1f}, cuidado! você está com Obesidade grau II (grave)​".format(imc))
elif imc > 40:
  print("seu imc é {:.1f}, cuidado! você está com Obesidade grau III (mórbida)​".format(imc))
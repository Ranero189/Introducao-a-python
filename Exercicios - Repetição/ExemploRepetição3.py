# test

compra_confirmada= True
dados_compra = "compra ok"
for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviados por email")
        break
else:
    print("Falha na compra")
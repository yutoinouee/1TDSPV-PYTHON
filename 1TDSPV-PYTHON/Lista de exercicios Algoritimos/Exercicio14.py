avista = float(input("Valor à vista: "))
parcela = float(input("Valor da parcela: "))

total_parcelado = parcela * 10

desconto = total_parcelado - avista
percentual = (desconto / total_parcelado) * 100

print("Desconto (%):", percentual)
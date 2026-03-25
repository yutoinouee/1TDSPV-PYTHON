dias = int(input("Dias úteis no mês: "))
horas_trabalhadas = float(input("Total de horas trabalhadas: "))
valor_hora = float(input("Valor por hora: "))

horas_normais = dias * 8

if horas_trabalhadas > horas_normais:
    horas_extras = horas_trabalhadas - horas_normais
    valor_extra = horas_extras * (valor_hora * 1.5)
else:
    horas_extras = 0
    valor_extra = 0

salario_normal = horas_normais * valor_hora
salario_final = salario_normal + valor_extra

print("Horas extras:", horas_extras)
print("Valor de hora extra: R$", valor_extra)
print("Salário final: R$", salario_final)
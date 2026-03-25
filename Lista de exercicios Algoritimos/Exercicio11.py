antes = float(input("Salário antes: "))
depois = float(input("Salário depois: "))

percentual = ((depois - antes) / antes) * 100

print("Percentual de aumento:", percentual, "%")
preco = float(input("Preço do produto: "))
percentual = float(input("Percentual (%): "))

desconto = preco * (percentual / 100)
novo_preco = preco - desconto

print("Desconto: R$", desconto)
print("Novo preço: R$", novo_preco)

# Para aumento:
aumento = preco * (percentual / 100)
preco_aumentado = preco + aumento

print("Preço com aumento: R$", preco_aumentado)
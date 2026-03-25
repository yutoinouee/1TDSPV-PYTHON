rm = int(input("Digite o RM: "))

soma = 0

soma += rm % 10
rm //= 10

soma += rm % 10
rm //= 10

soma += rm % 10
rm //= 10

soma += rm % 10
rm //= 10

soma += rm % 10

print("Soma dos dígitos:", soma)
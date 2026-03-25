A = int(input("Digite A: "))
B = int(input("Digite B: "))

if B == 0:
    print("Não existe divisão por zero")
elif A % B == 0:
    print("A é divisível por B")
else:
    print("A não é divisível por B")
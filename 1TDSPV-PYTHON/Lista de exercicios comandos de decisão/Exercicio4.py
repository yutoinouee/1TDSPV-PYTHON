time1 = input("Nome do primeiro time: ")
gols1 = int(input("Gols do primeiro time: "))

time2 = input("Nome do segundo time: ")
gols2 = int(input("Gols do segundo time: "))

if gols1 > gols2:
    print("Vencedor:", time1)
elif gols2 > gols1:
    print("Vencedor:", time2)
else:
    print("EMPATE")
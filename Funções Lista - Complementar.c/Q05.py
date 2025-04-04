def gerador_tabuada(numero):
    print(f"Tabuada do {numero}:\n")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Digite um número para ver sua tabuada: "))
gerador_tabuada(num)
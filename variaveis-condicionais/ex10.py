numero = int(input("Digite um número inteiro maior que 1: "))

if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"O número {numero} não é primo.")
            break
    else:
        print(f"O número {numero} é primo.")
else:
    print("Por favor, digite um número maior que 1.")
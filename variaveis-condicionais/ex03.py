valor = float(input("Digite o valor total das mercadorias compradas: R$"))

if valor < 500:
    print("Não há imposto.")
else:
    imposto = (valor - 500) * 0.50
    print(f"O valor do imposto é: R${imposto:.2f}")

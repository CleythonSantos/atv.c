dias = int(input("Digite o número de dias de aluguel: "))
km = float(input("Digite a quantidade de quilômetros rodados: "))
custo = dias * 90
if km > 100:
    custo += (km - 100) * 12
    print(f"Valor total a pagar: R${custo:.2f}")
salario_inicial = float(input("Digite o salário inicial: R$"))
anos = int(input("Digite o número de anos: "))


salario_atual = salario_inicial * (2 ** anos)

print(f"O salário após {anos} anos será: R${salario_atual:.2f}")
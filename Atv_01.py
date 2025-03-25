1. cálculo de médias

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media_aritmetica = (nota1 + nota2 + nota3) / 3
    media_ponderada_1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / 7
    media_ponderada_2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / 5
    
    print(f"Média Aritmética: {media_aritmetica:.2f}")
    print(f"Média Ponderada (2,2,3): {media_ponderada_1:.2f}")
    print(f"Média Ponderada (1,2,2): {media_ponderada_2:.2f}")

# 2. Conversão de segundos para dias, horas e minutos

    segundos = int(input("Digite o tempo em segundos: "))
    dias = segundos // 86400
    segundos %= 86400
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    
    print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")

# 3. Cálculo de imposto sobre mercadorias

    valor = float(input("Digite o valor total das mercadorias: "))
    if valor > 500:
        imposto = (valor - 500) * 0.5
    else:
        imposto = 0
    print(f"Imposto a ser pago: R${imposto:.2f}")

# 4. Cálculo do aluguel de carro

    dias = int(input("Digite o número de dias de aluguel: "))
    km = float(input("Digite a quantidade de quilômetros rodados: "))
    custo = dias * 90
    if km > 100:
        custo += (km - 100) * 12
    print(f"Valor total a pagar: R${custo:.2f}")

# 5. Impressão dos 100 primeiros números naturais

    for i in range(100):
        print(i, end=" ")
    print()

# 6. Geração de números primos

    primos = []
    num = 2
    while len(primos) < 100:
        for p in primos:
            if num % p == 0:
                break
        else:
            primos.append(num)
        num += 1
    print(primos)

# 7. Diferença entre quadrados de ímpares

    num = int(input("Digite um número ímpar: "))
    if num % 2 == 0:
        print("O número deve ser ímpar.")
        return
    anterior = (num - 2) ** 2
    proximo = (num + 2) ** 2
    print(f"Diferença: {proximo - anterior}")

# 8. Conversão de temperatura

    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}")

# 9. Identificação do maior e menor número

    numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(3)]
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")

# 10. Verificação de número primo

    num = int(input("Digite um número inteiro maior que 1: "))
    if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        print("É primo")
    else:
        print("Não é primo")

# 11. Sistema de login

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuario == senha:
        print("Erro: Usuário e senha não podem ser iguais!")
    else:
        print("Login bem-sucedido!")

# 12. Média de alunos por turma

    turmas = int(input("Digite a quantidade de turmas: "))
    total_alunos = int(input("Digite o total de alunos: "))
    media = total_alunos / turmas
    print(f"Média de alunos por turma: {media:.2f}")
    if media > 40:
        print("Alerta: Turma com mais de 40 alunos!")

# 13. Cálculo de aumento salarial

    salario = float(input("Digite o salário inicial: "))
    anos = int(input("Digite o número de anos: "))
    aumento = 0.05
    for _ in range(anos):
        salario += salario * aumento
        aumento *= 2
    print(f"Salário após {anos} anos: R${salario:.2f}")

# Chamadas para teste das funções
if _name_ == "_main_":
    calcular_medias()
    converter_tempo()
    calcular_imposto()
    calcular_aluguel()
    imprimir_naturais()
    gerar_primos()
    diferenca_quadrados()
    converter_temperatura()
    maior_menor()
    eh_primo()
    sistema_login()
    media_alunos()
    calcular_salario()
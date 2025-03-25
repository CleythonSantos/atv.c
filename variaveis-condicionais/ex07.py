numero = int(input("Digite um número ímpar: "))

if numero % 2 == 1:
    numero_anterior = numero - 2
    numero_proximo = numero + 2
    
    quadrado_anterior = numero_anterior ** 2
    quadrado_proximo = numero_proximo ** 2
    
    diferenca = quadrado_proximo - quadrado_anterior
    
    print(f"A diferença entre o quadrado do próximo número ímpar e o quadrado do número anterior é: {diferenca}")
else:
    print("O número digitado não é ímpar. Tente novamente.")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def calculadora():
    print("Selecione a operação:")
    print("+ | Soma")
    print("- | Subtração")
    print("* | Multiplicação")
    print("/ | Divisão")
    
    opcao = input("Escolha a opção da sua operação: ")
    
    if opcao in ('+', '-', '*', '/'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == '+':
            print(f"Resultado: {soma(num1, num2)}")
        elif opcao == '-':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif opcao == '*':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif opcao == '/':
            print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Opção inválida!")

calculadora()
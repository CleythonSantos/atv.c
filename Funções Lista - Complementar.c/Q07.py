import random

def Simulador_dados():
    return random.randint(1, 6)
resultado = Simulador_dados()
print(f"O número sorteado foi: {resultado}")
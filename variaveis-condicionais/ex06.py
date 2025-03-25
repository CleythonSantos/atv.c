primos = []
numero = 2  
while len(primos) < 100:
    is_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            is_primo = False
            break
    if is_primo:
        primos.append(numero)
    numero += 1
    
print("Os 100 primeiros números primos são:")
print(primos)
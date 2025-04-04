def converter_km_para_milhas(km):
    milhas = km * 0.621371
    return milhas

def converter_metros_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

def converter_litros_para_mililitros(litros):
    mililitros = litros * 1000
    return mililitros

km = float(input("Digite a distância em quilômetros: "))
metros = float(input("Digite a distância em metros: "))
litros = float(input("Digite o volume em litros: "))

milhas = converter_km_para_milhas(km)
centimetros = converter_metros_para_centimetros(metros)
mililitros = converter_litros_para_mililitros(litros)

print()
print("Resultado das conversões:")
print(km, "quilômetros = ", milhas, "milhas")
print(metros, "metros = ", centimetros, "centímetros")
print(litros, "litros = ", mililitros, "mililitros")
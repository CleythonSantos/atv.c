segundos = int(input("Digite o tempo em segundos: "))
dias = segundos // 86400
segundos %= 86400
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60
    
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")
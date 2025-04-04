def contador_vogais(texto):
    vogais = "aeiouAEIOU"
    total_vogais = 0
    
    for char in texto:
        if char in vogais:
            total_vogais += 1
    
    return total_vogais

frase = input("Digite uma palavra ou frase: ")
total = contador_vogais(frase)
print("Total de vogais:", total)
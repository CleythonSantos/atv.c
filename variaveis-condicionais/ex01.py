nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
    
media_aritmetica = (nota1 + nota2 + nota3) / 3
media_ponderada_1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / 7
media_ponderada_2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / 5
    
print(f"Média Aritmética: {media_aritmetica:.2f}")
print(f"Média Ponderada (2,2,3): {media_ponderada_1:.2f}")
print(f"Média Ponderada (1,2,2): {media_ponderada_2:.2f}")
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return media, "Aprovado - Exelente guerreiro(a)"
    else:
        return media, "Reprovado - se fudeu kkk"

n1 = float(input("Digite a primeira nota: ").replace(",", "."))
n2 = float(input("Digite a segunda nota: ").replace(",", "."))
n3 = float(input("Digite a terceira nota:").replace(",", "."))

media, status = calcular_media(n1, n2, n3)
print(f"Média: {media:.2f}".replace(".", ",") + f" - Aluno: {status}")
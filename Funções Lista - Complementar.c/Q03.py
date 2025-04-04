def Contagem_de_Caracteres(frase):
    
    return len(frase.replace(" ", ""))

frase_usuario = input("Digite uma frase: ")
quantidade = Contagem_de_Caracteres(frase_usuario)
print(f"A frase possui {quantidade} caracteres.")
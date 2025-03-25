num_turmas = int(input("Digite a quantidade de turmas: "))
total_alunos = int(input("Digite a quantidade total de alunos: "))

media_alunos = total_alunos / num_turmas

print(f"A média de alunos por turma é: {media_alunos:.2f}")

if media_alunos > 40:
    print("Aviso! A média de alunos por turma é maior que 40.")
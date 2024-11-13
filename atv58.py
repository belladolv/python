total_alunos = 0
soma_idades = 0

while True:
    idade = int(input("Digite a idade do aluno (999 para parar): "))
    if idade == 999:
        break
    total_alunos += 1
    soma_idades += idade

if total_alunos > 0:
    media_idade = soma_idades / total_alunos
    print(f"Total de alunos: {total_alunos}")
    print(f"Média de idade do grupo: {media_idade:.2f}")
else:
    print("Nenhum aluno foi registrado.")

def Situacao(media):
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def Media(nota1, nota2):
    return (nota1 + nota2) / 2

# Leitura dos dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Chamada da função Media e Situacao
media = Media(nota1, nota2)
situacao = Situacao(media)

print(f"A média do aluno é: {media:.2f}")
print(f"Situação do aluno: {situacao}")

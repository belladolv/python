def Media(nota1, nota2):
    return (nota1 + nota2) / 2

# Leitura dos dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Chamada da função e exibição do resultado
media = Media(nota1, nota2)
print(f"A média do aluno é: {media:.2f}")

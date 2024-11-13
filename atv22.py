ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2024
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f"Faltam {18 - idade} anos para o seu alistamento militar.")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
else:
    print("Você deve se alistar este ano.")

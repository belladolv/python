ano_nascimento = int(input("Qual o seu ano de nascimento? "))
ano_atual = 2024
idade = ano_atual - ano_nascimento

print(f"Sua idade é {idade} anos.")
if idade >= 18:
    print("Você pode votar!")
else:
    print("Você não pode votar ainda.")

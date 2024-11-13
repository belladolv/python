# Listas para armazenar os dados
nomes = []
sexos = []
salarios = []

# Leitura dos dados
for i in range(5):
    nome = input(f"Digite o nome do funcionário {i+1}: ")
    sexo = input(f"Digite o sexo (M/F) do funcionário {i+1}: ")
    salario = float(input(f"Digite o salário do funcionário {i+1}: "))
    
    nomes.append(nome)
    sexos.append(sexo)
    salarios.append(salario)

# Exibição das mulheres com salário maior que 5000
print("\nFuncionárias mulheres com salário superior a R$5000:")
for i in range(5):
    if sexos[i] == "F" and salarios[i] > 5000:
        print(f"{nomes[i]} - R${salarios[i]:.2f}")

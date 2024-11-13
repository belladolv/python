def ParOuImpar(n):
    if n % 2 == 0:
        print(f"O número {n} é PAR.")
    else:
        print(f"O número {n} é ÍMPAR.")

# Leitura dos dados
n = int(input("Digite um número: "))

# Chamada da função
ParOuImpar(n)

def Contador(inicio, fim, incremento):
    for i in range(inicio, fim + 1, incremento):
        print(i, end=" >> ")
    print("FIM")

# Leitura dos dados
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
incremento = int(input("Digite o valor do incremento: "))

# Chamada da função
Contador(inicio, fim, incremento)

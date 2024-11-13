def Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" >> ")
        a, b = b, a + b
    print("FIM")

# Leitura dos dados
n = int(input("Digite quantos termos da sequência de Fibonacci deseja mostrar: "))

# Chamada da função
Fibonacci(n)

# Inicializa a lista com os dois primeiros termos da sequência de Fibonacci
fibonacci = [1, 1]

# Gera os próximos 8 termos da sequência
for i in range(2, 10):
    # O próximo número é a soma dos dois últimos termos
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

# Exibe os 10 primeiros termos da sequência de Fibonacci
print("Os 10 primeiros termos da sequência de Fibonacci são:")
print(fibonacci)

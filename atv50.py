import random

numeros = [random.randint(0, 10) for _ in range(20)]
print(f"Números sorteados: {numeros}")

acima_5 = sum(1 for num in numeros if num > 5)
divisiveis_3 = sum(1 for num in numeros if num % 3 == 0)

print(f"Números acima de 5: {acima_5}")
print(f"Números divisíveis por 3: {divisiveis_3}")

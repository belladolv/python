import random

numero_sorteado = random.randint(1, 5)
numero_jogador = int(input("Tente adivinhar o número sorteado entre 1 e 5: "))

if numero_jogador == numero_sorteado:
    print("Você acertou! O número sorteado foi", numero_sorteado)
else:
    print(f"Você errou. O número sorteado foi {numero_sorteado}.")

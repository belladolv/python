import random

opcoes = ["Pedra", "Papel", "Tesoura"]
jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
computador = random.choice(opcoes)

print(f"Computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "Pedra" and computador == "Tesoura") or \
     (jogador == "Papel" and computador == "Pedra") or \
     (jogador == "Tesoura" and computador == "Papel"):
    print("Você venceu!")
else:
    print("Você perdeu!")

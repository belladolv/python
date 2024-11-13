import random

numero_sorteado = random.randint(1, 10)
tentativas = 4
acertou = False

print("Bem-vindo ao jogo! Tente adivinhar o número entre 1 e 10.")
while tentativas > 0 and not acertou:
    palpite = int(input(f"Você tem {tentativas} tentativas restantes. Digite seu palpite: "))
    
    if palpite == numero_sorteado:
        acertou = True
        print("Parabéns! Você acertou o número!")
    elif palpite < numero_sorteado:
        print("O número sorteado é maior. Tente novamente.")
    else:
        print("O número sorteado é menor. Tente novamente.")
    
    tentativas -= 1

if not acertou:
    print(f"Você perdeu! O número sorteado era {numero_sorteado}.")

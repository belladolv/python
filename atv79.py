algoritmo "pares_posicoes"
inicio
   vetor numeros[10]
   
   // Leitura dos 10 números
   para i de 1 até 10 passo 1 faça
      escreva("Digite o ", i, "º número: ")
      leia(numeros[i])
   fimpara

   // Mostrando os números pares e suas posições
   escreva("Números pares e suas posições: ")
   para i de 1 até 10 passo 1 faça
      se numeros[i] % 2 = 0 então
         escreva("Número: ", numeros[i], " na posição: ", i, " | ")
      fimse
   fimpara
fimalgoritmo

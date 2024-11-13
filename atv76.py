algoritmo "vetor_aleatorio"
inicio
   // Vetor para armazenar os números
   vetor numeros[7]
   
   // Preenchendo o vetor com números aleatórios
   para i de 1 até 7 passo 1 faça
      numeros[i] <- aleatorio(1, 100) // Gerando números aleatórios entre 1 e 100
   fimpara

   // Mostrando os números gerados
   escreva("Valores gerados: ")
   para i de 1 até 7 passo 1 faça
      escreva(numeros[i], " ")
   fimpara
fimalgoritmo

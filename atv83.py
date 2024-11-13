algoritmo "vetor_ordenado_aleatorio"
inicio
   vetor numeros[20]
   vetor ordenado[20]
   
   // Preenchendo o vetor com números aleatórios entre 0 e 99
   para i de 1 até 20 passo 1 faça
      numeros[i] <- aleatorio(0, 99)
   fimpara

   // Mostrando os números gerados
   escreva("Valores gerados: ")
   para i de 1 até 20 passo 1 faça
      escreva(numeros[i], " ")
   fimpara

   // Copiando os valores para o vetor ordenado
   para i de 1 até 20 passo 1 faça
      ordenado[i] <- numeros[i]
   fimpara

   // Ordenando o vetor em ordem crescente (Bubble Sort)
   para i de 1 até 19 passo 1 faça
      para j de 1 até 19 passo 1 faça
         se ordenado[j] > ordenado[j+1] então
            // Troca os valores
            temp <- ordenado[j]
            ordenado[j] <- ordenado[j+1]
            ordenado[j+1] <- temp
         fimse
      fimpara
   fimpara

   // Mostrando os números ordenados
   escreva("\nValores ordenados: ")
   para i de 1 até 20 passo 1 faça
      escreva(ordenado[i], " ")
   fimpara
fimalgoritmo

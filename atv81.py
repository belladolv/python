algoritmo "idades_media"
inicio
   vetor idades[8]
   soma <- 0
   maiorIdade <- 0
   posMaiorIdade[8] <- 0
   contadorMaior25 <- 0

   // Leitura das idades
   para i de 1 até 8 passo 1 faça
      escreva("Digite a ", i, "º idade: ")
      leia(idades[i])
      soma <- soma + idades[i]
      
      // Encontrando maior idade
      se idades[i] > maiorIdade então
         maiorIdade <- idades[i]
      fimse

      // Contando maiores de 25
      se idades[i] > 25 então
         contadorMaior25 <- contadorMaior25 + 1
      fimse
   fimpara

   // Calculando a média
   mediaIdade <- soma / 8

   // Mostrando os resultados
   escreva("Média de idade: ", mediaIdade, "\n")
   escreva("Pessoas com mais de 25 anos: ", contadorMaior25, "\n")
   escreva("Maior idade: ", maiorIdade, "\n")

   // Mostrando posições da maior idade
   escreva("Posições da maior idade: ")
   para i de 1 até 8 passo 1 faça
      se idades[i] = maiorIdade então
         escreva(i, " ")
      fimse
   fimpara
fimalgoritmo

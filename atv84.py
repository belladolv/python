algoritmo "nomes_idades_menores_de_idade"
inicio
   vetor nomes[9]
   vetor idades[9]
   
   // Leitura dos nomes e idades
   para i de 1 até 9 passo 1 faça
      escreva("Digite o nome da ", i, "ª pessoa: ")
      leia(nomes[i])
      escreva("Digite a idade de ", nomes[i], ": ")
      leia(idades[i])
   fimpara

   // Mostrando as pessoas menores de idade
   escreva("\nPessoas menores de idade:\n")
   para i de 1 até 9 passo 1 faça
      se idades[i] < 18 então
         escreva("Nome: ", nomes[i], " - Idade: ", idades[i], "\n")
      fimse
   fimpara
fimalgoritmo

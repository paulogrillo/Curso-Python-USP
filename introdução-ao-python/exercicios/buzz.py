#Exercícios 3 - FizzBuzz parcial, parte 2
#Receba um número inteiro na entrada e imprima

#Buzz

#se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input('Digite um inteiro: '))

if not (numero%5) :
    print("É múltiplo de 5")
else:
    print("Não é múltiplo de 5")
#Receba um número inteiro na entrada e imprima 

#Fizz

 #se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input('Digite um número: '))
if (numero%3) == 0:
  print("Fizz")
else:
  print(numero)
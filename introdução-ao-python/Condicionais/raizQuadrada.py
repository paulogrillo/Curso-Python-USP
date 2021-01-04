#Raiz de uma equação do segundo grau
import math #Import math

#Entrada de dados
a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))

#Calculo do delta
delta = b ** 2 - 4 * a * c

#Condicionais
if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é: ", raiz1)
else:
    if delta < 0:
        print("Essa equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)

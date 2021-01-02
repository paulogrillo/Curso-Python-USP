################# Exercício 1

#Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

#Observação: a saída deve estar no formato: "perímetro: x - área: y"

#Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

#Exemplo:

#Entrada de Dados: 
#Digite o valor correspondente ao lado de um quadrado: 3

#Saída de Dados:
#perímetro: 12 - área: 9

#Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez
############################################################################
############################################################################
############################## [Opção escolhida] #############################
############################################################################
l = int(input("Digite o valor correspondente ao lado de um quadrado:"))
x = l * 4
y = l * l
print ("area: ", x)
print ("perimetro: ", y)

# Opção 1
# lquadrado = int(raw_input("Digite o valor correspondente ao lado de um quadrado: "))
# x = lquadrado * 4
# y = lquadrado * lquadrado
# print "area: ", x
# print "perimetro: ", y

# Opção 2
# lado=a = int(input("Digite o lado do quadrado: ? "))
# perimetro  = lado *4
# area = lado * lado
# print("perimetro:", perimetro, "-", " area:", area)
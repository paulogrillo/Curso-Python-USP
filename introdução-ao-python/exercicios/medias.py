# Exercício 2
# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:
# Exemplo:
# Entrada de Dados:
# Digite a primeira nota: 4
# Digite a segunda nota: 5
# Digite a terceira nota: 6
# Digite a quarta nota: 7
# Saída de Dados:
# A média aritmética é 5.5

# Dica: uso do print
# Quando você usa o comando print para imprimir mais de uma coisa, ele inclui automaticamente espaços entre os argumentos impressos. Cuidado para não incluir espaços demais na sua resposta! O corretor perceberá e tirará pontos


n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))
n3 = int(input("Digite a terceira nota:"))
n4 = int(input("Digite a quarta nota:"))

soma = n1+n2+n3+n4
media = soma / 4

print("A média aritmética é", media)
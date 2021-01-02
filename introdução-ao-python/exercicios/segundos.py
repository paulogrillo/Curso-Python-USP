# Exercício 2
# Este é o desafio do vídeo "Entrada de Dados".

# Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

# Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

# Exemplo:

# Entrada de Dados:
# Por favor, entre com o número de segundos que deseja converter: 178615

# Saída de Dados:
# 2 dias, 1 horas, 36 minutos e 55 segundos.

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")

# Opção 1

# segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
# print (segundos)
# horas = segundos // 3600
# segundosRestantes = segundos %3600
# minutos = segundosRestantes // 60
# finalSegundos = segundosRestantes % 60
# dias = horas // 1440
# finalMinutos = dias // horas
# print ("dias",dias,"horas", horas, "minutos",finalMinutos, "segundos",finalSegundos)

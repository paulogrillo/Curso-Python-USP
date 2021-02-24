tempoDeJogo = int(input("Quanto tempo temos já jogados?"))
tempoRestante = tempoDeJogo * 100 / 90

if tempoDeJogo <= 90:
    print("- Ainda tem jogo pela frente")
    print("- Ótimo!", tempoRestante)
else:
    print("O jogo está perto de acabar..")
class Pilha(object):
    def __init__(self):
        self.elementos = []

    def empilha(self, elemento):
        self.elementos.append(elemento)

    def desempilha(self):
        return self.elementos.pop()

    def vazio(self):
        return len(self.elementos) == 0

class Fila(object):
    def __init__(self):
        self.normal = Pilha()
        self.invertida = Pilha()

    def insere(self, elemento):
        transfere(self.invertida, self.normal)
        self.normal.empilha(elemento)

    def remove(self):
        transfere(self.normal, self.invertida)
        return self.invertida.desempilha()

    def vazio(self):
        return self.normal.vazio() and self.invertida.vazio()

def transfere(origem, destino):
    while (not origem.vazio()):
        destino.empilha(origem.desempilha())
class Matriz(object):

    def __init__(self, nova_matriz):
        self.matriz = nova_matriz

    def elemento(self, i, j):
        return self.matriz[i][j]

    @property
    def num_colunas(self):
        return len(self.matriz[0])

    def ultima_linha(self):
        return self.linha(-1)

    def linha(self, i):
        return self.matriz[i]

    def e_matriz_espiral(self):
        if self.num_colunas == 2:
            return lista_ordenada(self.linha(0)) and lista_ordenada(self.ultima_linha(), reverso=True)
        return True

def lista_ordenada_sequencialmente(lista, reverso = False):
    return lista == sorted(lista, reverse=reverso)

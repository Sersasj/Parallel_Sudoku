# pip3 install py-sudoku

# Implementação do grafo
class Grafo:
    def __init__(self, V, Adj, tam):
        self.V = V
        self.Adj = Adj
        self.tam = tam


class Vertice:
    def __init__(self, indice, d, pai, cor):
        self.indice = indice
        self.d = d
        self.pai = pai
        self.cor = cor

from sudoku import Sudoku
tam = 2
puzzle = Sudoku(tam).difficulty(0.5)
solution = puzzle.solve()
solution.show()
print(puzzle.board)

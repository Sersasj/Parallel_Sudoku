# pip3 install py-sudoku

# Implementação do grafo
class Graph:
    def __init__(self, V, Adj, edges, total_nodes):
        self.V = V
        self.Adj = Adj
        self.edges = edges
        self.total_nodes = total_nodes


class Node:
    def __init__(self, index, data, connections):
        self.index = index
        self.data = data
        self.connections = connections
    
    def add_neighbour(self, neighbour, weight):
        if neighbour not in self.connections:
            self.connections[neighbour.index] = weight

    # setter
    def setData(self, data) : 
        self.data = data 

    #getter
    def getConnections(self) : 
        return self.connections

    def getID(self) : 
        return self.index
    
    def getData(self) : 
        return self.data

    def getWeight(self, neighbour) : 
        return self.connections[neighbour.index]

    def __str__(self) : 
        return str(self.data) + " Connected to : "+ \
         str([x.data for x in self.connections])

from sudoku import Sudoku
tam = 2
puzzle = Sudoku(tam).difficulty(0.5)
puzzle.show()
solution = puzzle.solve()
#solution.show()
print(puzzle.board)

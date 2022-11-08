# pip3 install py-sudoku
import numpy as np
# Implementação do grafo
class Graph:
    def __init__(self, nodes, Adj, edges, total_nodes):
        self.nodes = nodes
        self.Adj = Adj
        self.edges = edges
        self.total_nodes = total_nodes

# Node = Vertice
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

    # getter
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
# cria o grafo
graph = Graph([], [], [], tam**4)
for i in range(graph.total_nodes):
    graph.Adj.append([])
#two vertices are connected by an edge if the cells that they correspond to are in the same column, row or 3x3 box.
i = 0    
aux = np.arange(0,tam**4).reshape((tam**2, tam**2))

for line in range(tam**2):
    for column in range(tam**2):
  
        #print(puzzle.board[0:line,0])
        graph.nodes.append(Node(i, aux[line][column],np.concatenate(aux[0:line,column],aux[line+1:tam**2,column])))
        i += 1
# puzzle.board[0:line][column] + puzzle.board[line+1:tam_list][column]
#                       + puzzle.board[line][0:column] + puzzle.board[line][column+1:tam_list]
#puzzle.board[0:line,line+1:tam**2][column]+ puzzle.board[line][0:column,column+1:tam**2]
for node in graph.nodes:
    
    print(node.getID())


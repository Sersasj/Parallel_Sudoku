# pip3 install py-sudoku
import numpy as np
from copy import deepcopy
# Implementação do grafo
class Graph:
    def __init__(self, nodes, Adj, edges, total_nodes):
        self.nodes = nodes
        self.Adj = Adj
        self.edges = edges
        self.total_nodes = total_nodes

# Node = Vertice
class Node:
    def __init__(self, index, data, possible_data, connections):
        self.index = index
        self.data = data
        self.possible_data = possible_data
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
i = 0    
aux = np.arange(0,tam**4).reshape((tam**2, tam**2))
# Liga todas as possibilidades de vértice
for line in range(tam**2):
    for column in range(tam**2):  
        if line % tam == 0 and column % tam == 0:
            box_aux = np.concatenate((aux[line:line+tam,column:column+tam]),axis=None)
            
        box = np.delete(box_aux,np.where(box_aux == aux[line,column]))
        connections = np.concatenate((aux[0:line,column], aux[line+1:tam**2,column], # Coluna
                                      aux[line,0:column], aux[line,column+1:tam**2], # Linha
                                      box),# box 
                                     axis=None)        
        connections = np.unique(connections)
        
        if puzzle.board[line][column] ==  None:
            graph.nodes.append(Node(i, puzzle.board[line][column], np.arange(1,tam**2 + 1, 1), connections))                                                                    
        else:
            graph.nodes.append(Node(i, puzzle.board[line][column], [puzzle.board[line][column]], connections))   
                                                 
        i += 1
def contraint(graph):       
    # Contraint 1 - se um node tem só 1 possibilidade tira ela de todos as conexões
    for node in range(tam**4):
        if len(graph.nodes[node].possible_data) == 1:
            for connection in graph.nodes[node].connections:
                print("Antes", graph.nodes[connection].possible_data)
                graph.nodes[connection].possible_data = np.delete(graph.nodes[connection].possible_data, np.where(graph.nodes[connection].possible_data == graph.nodes[node].possible_data))
                print("Depois", graph.nodes[connection].possible_data)

    # Constraint 2 -  se um node só tem 1 possibilidade torna ela o dado
    for node in range(tam**4):
        if len(graph.nodes[node].possible_data) == 1 and graph.nodes[node].data == None:
            print("entrouu",graph.nodes[node].index , graph.nodes[node].possible_data[0])
            graph.nodes[node].data = graph.nodes[node].possible_data[0]
            
finish = 0             
def search(graph):
    #print(len(graph.nodes[2].possible_data))
    
    count = 0
    for i in range(tam**4):
        if len(graph.nodes[i].possible_data) == 1:
            count += 1 
    if count ==  tam**4:
        finish = -1
for i in range(10):
    contraint(graph)        
    search(graph)    

# Transfere conteúdo do grafo para o puzzle
count = 0
for line in range(tam**2):
    for column in range(tam**2):  
        puzzle.board[line][column] =  graph.nodes[count].data
        count +=1 
puzzle.show()

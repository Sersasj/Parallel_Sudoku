# pip3 install py-sudoku
from sudoku import Sudoku
import numpy as np
from copy import deepcopy
from random import randint
from random import choice


# Implementação do grafo
class Graph:

  def __init__(self, nodes, total_nodes):
    self.nodes = nodes
    self.total_nodes = total_nodes


# Node = Vertice
class Node:

  def __init__(self, index, data, possible_data, connections):
    self.index = index
    self.data = data
    self.possible_data = possible_data
    self.connections = connections





tam = 3
puzzle = Sudoku(tam).difficulty(0.9)
puzzle.show()
solution = puzzle.solve()
# Cria o grafo
graph = Graph([], tam**4)
index = 0
aux = np.arange(0, tam**4).reshape((tam**2, tam**2))
box_aux = []
# Liga todas as possibilidades de vértice
for line in range(tam**2):
  for column in range(tam**2):
    if line % tam == 0 and column % tam == 0:
      box_aux.append(
        np.concatenate((aux[line:line + tam, column:column + tam]), axis=None))
    for i in range(len(box_aux)):
      if aux[line, column] in box_aux[i]:
        box_id = i
    box = np.delete(box_aux[box_id],
                    np.where(box_aux[box_id] == aux[line, column]))
    connections = np.concatenate(
      (
        aux[0:line, column],
        aux[line + 1:tam**2, column],  # Coluna
        aux[line, 0:column],
        aux[line, column + 1:tam**2],  # Linha
        box),  # box 
      axis=None)
    connections = np.unique(connections)

    if puzzle.board[line][column] == None:
      graph.nodes.append(
        Node(index, puzzle.board[line][column], np.arange(1, tam**2 + 1, 1),
             connections))
    else:
      graph.nodes.append(
        Node(index, puzzle.board[line][column], [puzzle.board[line][column]],
             connections))

    index += 1



def contraint(graph):
  first = 0
  print("Entrou")
  while(check_constraint(graph) or first == 0):
      first += 1
      # Contraint 1 - se um node tem só 1 possibilidade tira ela de todos as conexões
      for node in range(tam**4):
        if len(graph.nodes[node].possible_data) == 1:
          for connection in graph.nodes[node].connections:
            graph.nodes[connection].possible_data = np.delete(
              graph.nodes[connection].possible_data,
              np.where(graph.nodes[connection].possible_data ==
                          graph.nodes[node].possible_data[0]))
    
      # Constraint 2 -  se um node só tem 1 possibilidade torna ela o dado
      for node in range(tam**4):
        if len(graph.nodes[node].possible_data
               ) == 1 and graph.nodes[node].data == None:
          graph.nodes[node].data = graph.nodes[node].possible_data[0]
          for connection in graph.nodes[node].connections:
            graph.nodes[connection].possible_data = np.delete(
              graph.nodes[connection].possible_data,
              np.where(graph.nodes[connection].possible_data ==
                          graph.nodes[node].possible_data[0]))    

finish = 0

def check_constraint(graph):
    for node in range(tam**4):
        if len(graph.nodes[node].possible_data) == 1 and graph.nodes[node].data == None:
            return True    
    return False


graph_backtrack = []

def random(graph):
    min_id = None

    for node in range(tam**4):
        if graph.nodes[node].data == None:
            if min_id == None:
                min_id = node
            elif(len(graph.nodes[node].possible_data) < len(graph.nodes[min_id].possible_data)):
                min_id = node
    if  min_id == None or len(graph.nodes[min_id].possible_data) == 0 :
        return
     
    random_index = randint(0,len(graph.nodes[min_id].possible_data)-1)
    graph.nodes[min_id].data = graph.nodes[min_id].possible_data[random_index]
    graph_backtrack.append(deepcopy(graph))        

    # Remove dos conectados
    for connection in graph.nodes[min_id].connections:
      graph.nodes[connection].possible_data = np.delete(
        graph.nodes[connection].possible_data,
        np.where(graph.nodes[connection].possible_data ==
                    graph.nodes[min_id].possible_data[random_index]))   
         

        
        
#Transfere conteúdo do grafo para o puzzle
def print_puzzle(graph):
    count = 0
    for line in range(tam**2):
      for column in range(tam**2):
        puzzle.board[line][column] = graph.nodes[count].data
        count += 1
    puzzle.show()
def verify_error(graph):
    count = 0
    for node in range(tam**4):
        #print(node, graph.nodes[node].index, graph.nodes[node].possible_data)

        if len(graph.nodes[node].possible_data) == 0:
            #print(graph.nodes[node].index, graph.nodes[node].possible_data[:])
            count += 1
    #print("Count = ", count)        
    if count > 0:
        return True  
    return False     
def verify_finish(graph):
    count = 0
    for node in range(tam**4):
        if graph.nodes[node].data != None:
            count += 1
    if count == tam**4 and verify_error(graph) == False:
        return True    
while(True):
  print(len(graph_backtrack))
  contraint(graph)
  print("CT")
  print_puzzle(graph)
  print("Random")
  random(graph)
  print_puzzle(graph) 

  if verify_error(graph):
      print("Back")
      graph = deepcopy(graph_backtrack[-1])
      del graph_backtrack[-1]

  if verify_finish(graph):
      break
  
print_puzzle(graph)
  
print("Solucao")
solution.show()
# 
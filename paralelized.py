# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:01:40 2022

@author: sergi
"""

import numpy as np

import sys
from sudoku import Sudoku
tam = 6 
puzzle = Sudoku(tam).difficulty(0.1)

for i in range(tam**2): 
    for j in range(tam**2):
        puzzle.board[i][j] =  int(0 if puzzle.board[i][j] is None else puzzle.board[i][j])
grid = puzzle.board
"""
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]
"""

def possible(row, column, number):
    global grid
    #Is the number appearing in the given row?
    for i in range(0,tam**2):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,tam**2):
        if grid[i][column] == number:
            return False
    
    #Is the number appearing in the given square?
    x0 = (column // tam) * tam
    y0 = (row // tam) * tam
    for i in range(0,tam):
        for j in range(0,tam):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,tam**2):
        for column in range(0,tam**2):
            if grid[row][column] == 0:
                for number in range(1,tam**2 + 1):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return
      
    print(np.matrix(grid))
    sys.exit()
    
def main():
    solve()    
if __name__ == "__main__":
    main()

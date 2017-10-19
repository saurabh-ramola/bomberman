from __future__ import print_function
from random import *
from colours import *           #colour module to give colours to list elements made with the help of internet
class Board():
    def __init__(self):
        self.arr = [["X" for x in range(64)] for y in range(22)] #making a list of lists
    def initialise_board(self):         #initial making of the board through list of lists 
        for x in range(2,20):
            for y in range(2,62):
                self.arr[x][y] =' '     #making all entries other than corners as spaces initially
        x = 4
        y = 6
        while x < 18:
            y = 6
            while y < 60:
                if x % 4 == 1 or x % 4 == 0:    #adding the relevant symbols as the walls
                 for i in range(0,4):
                    self.arr[x][y+i] = "X"
                    self.arr[x + 1][y+i] = "X"   
                y = y + 8
            x = x + 4
    def dispBoard(self):                    #displaying the board with the help of colours
        for i in range(22):
            for j in range(64):
                if self.arr[i][j] == 'X':
                    print(bcolors.GREEN + "X",end='')
                elif self.arr[i][j] == 'B':
                    print(bcolors.BLUE + "B",end='')
                elif self.arr[i][j] == 'E':
                    print(bcolors.MAGENTA + "E",end='')
                elif self.arr[i][j] == ' ':
                    print(bcolors.ENDC + ' ',end='')
                elif self.arr[i][j]>=0 and self.arr[i][j]<=3:
                    print(bcolors.HEADER + str(self.arr[i][j]),end='')
                else:
                    print(self.arr[i][j],end='')
            
            print('\n')
    





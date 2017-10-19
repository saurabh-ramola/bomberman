from board import *                         #importing board module to plant the intial position of the bomberman on the board
import sys
import time

class man(Board):
    def __init__(self):                     #declaring the properties that will be first to be declared when an object is made of "man" class
        Board.__init__(self)
        self.lExt = 2
        self.rExt = 5
        self.row = 2                
        self.num_bombs = 1
        self.type = 0
    def initialPos(self):                   #member funtion of class which calls another function from board class and makes the initial bomberman
        self.initialise_board()
        for i in range (0,4):
            self.arr[2][2+i] = "B"
            self.arr[3][2+i] = "B"
        
        


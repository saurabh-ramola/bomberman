from __future__ import print_function		#importing all the necessary inbuilt modules as well as the modules created by us for us to inherit here
from board import *
from bomb import *
from person import *
import sys
from enemy import *
import time
import threading
import termios
import os
import sys
import select
import tty

class Main(Board,man,Enemy):		#inheriting from the user defined classes
	def __init__(self):
		Board.__init__(self)
		man.__init__(self)
		Enemy.__init__(self)
		self.flag = 1
		self.count = 0
		self.check = 1

	def move_man(self):
		self.initial()				#calling the 
		
		global bombLt				#keeping track of the coordinates of the bomb
		global bombRt
		global bombRow
		def boom():
			self.count = self.count + 1	#for keeping time of the bomb
			if self.count != 4:		#implementing the bomb timer
				for i in range(0,4):
					self.arr[bombRow][bombLt+i] = 3-self.count
					self.arr[bombRow+1][bombLt+i] = 3-self.count
			else:
				self.count = 0
				self.check = 1
				b = checkEnemy(self.arr,bombRow,bombLt,bombRt,self.r,self.lt,self.rt)
				self.score = b*100			#killing nearby enemies
				a = checkBomber(self.arr,bombRow,bombLt,bombRt,self.row,self.lExt,self.rExt)	#if the bomber is near the bomb he gets killed
				if a == 1:
					print("YOU ARE DEAD")
					print('\n')
					print(self.score)
					print('\n')
					exit(1)
				for i in range (0,2):
					self.move_enemy()
				for i in range(0,4):
					self.arr[bombRow][bombLt+i] = " "
					self.arr[bombRow+1][bombLt+i] = " "
		def isData():
			return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

		old_settings = termios.tcgetattr(sys.stdin)
		def move_right():		#checking the conditions for the bMan to move right within the rules of the game as well as the conditions for its killing
			if self.lExt < 56:                
				if self.arr[self.row][self.rExt+4] != "X" and self.arr[self.row+1][self.rExt+4] != "X" :
					if self.count == 3:
						for i in range(0,4):
							self.arr[self.row][self.lExt+i] = " "
							self.arr[self.row+1][self.lExt+i] = " "
							self.arr[self.row][self.rExt+i+1] = "B"
							self.arr[self.row+1][self.rExt+i+1] = "B"
						self.rExt+=4
						self.lExt+=4
						boom()
					elif self.arr[self.row][self.rExt+1] == "E":
						for i in range(0,4):
							self.arr[self.row][self.lExt+i] = " "
							self.arr[self.row+1][self.lExt+i] = " "
							self.lExt+=1
							print("YOU ARE DEAD")
							print('\n')
							print(self.score)
							print('\n')
							exit(1)
					else:
						for i in range(1,5):
							if self.flag == 1:
								self.arr[self.row][self.rExt+i] = "B"
								self.arr[self.row+1][self.rExt+i] = "B"
								self.arr[self.row+1][self.lExt] = " "
								self.arr[self.row][self.lExt] = " "
								self.lExt += 1
							else:
								self.arr[self.row][self.rExt+i] = "B"
								self.arr[self.row+1][self.rExt+i] = "B"
								self.lExt += 1
						self.flag = 1	
						self.rExt += 4
				
		def move_left():		#checking the conditions for the bMan to move left within the rules of the game as well as the conditions for its killing
			if self.lExt >= 6:
				if self.arr[self.row][self.lExt-4] != "X" and self.arr[self.row+1][self.lExt-4] != "X" :
					if self.count == 3:
						for i in range(0,4):
							self.arr[self.row][self.rExt-i] = " "
							self.arr[self.row+1][self.rExt-i] = " "
							self.arr[self.row][self.lExt-i-1] = "B"
							self.arr[self.row+1][self.lExt-i-1] = "B"
						self.lExt-=4
						self.rExt-=4
						boom()
					elif self.arr[self.row][self.lExt-1] == "E":
						for i in range(0,4):
							self.arr[self.row][self.rExt-i] = " "
							self.arr[self.row+1][self.rExt-i] = " "
							self.rExt-=1
						
						print("YOU ARE DEAD")
						print('\n')
						print(self.score)
						print('\n')
						exit(1)
					else:
						for i in range(1,5):
							if self.flag == 1:
								self.arr[self.row][self.lExt-i] = "B"
								self.arr[self.row+1][self.lExt-i] = "B"
								self.arr[self.row][self.rExt] = " "
								self.arr[self.row+1][self.rExt] = " "
								self.rExt -= 1
							else:
								self.arr[self.row][self.lExt-i] = "B"
								self.arr[self.row+1][self.lExt-i] = "B"
								self.rExt -= 1
						self.flag = 1
						self.lExt -= 4    
				
		def move_up():			#checking the conditions for the bMan to move up within the rules of the game as well as the conditions for its killing
			if self.row-1 > 2:
				if self.arr[self.row-2][self.lExt] != "X" and self.arr[self.row-2][self.rExt] != "X":
					if self.count == 3:
						for i in range(0,4):
							self.arr[self.row+1][self.lExt+i] = " "
							self.arr[self.row][self.lExt+i] = " "
						self.row-=2
						boom()
					elif self.arr[self.row-2][self.lExt] == "E":
						for i in range(0,4):
							self.arr[self.row+1][self.lExt+i] = " "
							self.arr[self.row][self.lExt+i] = " "
						
						print("YOU ARE DEAD")
						print('\n')
						print(self.score)
						print('\n')
						exit(1)
					else:
						for i in range(0,4):
							if self.flag == 1:
								self.arr[self.row-2][self.lExt+i] = "B"
								self.arr[self.row-1][self.lExt+i] = "B"
								self.arr[self.row+1][self.lExt+i] = " "
								self.arr[self.row][self.lExt+i] = " "
							else:
								self.arr[self.row-2][self.lExt+i] = "B"
								self.arr[self.row-1][self.lExt+i] = "B"
						self.flag = 1
						self.row -= 2 
				  
		def move_down():		#checking the conditions for the bMan to move down within the rules of the game as well as the conditions for its killing
			if self.row + 2 < 19:
				if self.arr[self.row+2][self.lExt] != "X" and self.arr[self.row+2][self.rExt] != "X":
					if self.count == 3:
						for i in range(0,4):
							self.arr[self.row][self.lExt+i] = " "
							self.arr[self.row+1][self.lExt+i] = " "
						self.row+=2
						boom()
					elif self.arr[self.row+2][self.lExt] == "E":
						for i in range(0,4):
							self.arr[self.row][self.lExt+i] = " "
							self.arr[self.row+1][self.lExt+i] = " "
						
						print("YOU ARE DEAD")
						print('\n')
						print(self.score)
						print('\n')
						exit(1)
					else:
						for i in range(0,4):
							if self.flag == 1:
								self.arr[self.row+3][self.lExt+i] = "B"
								self.arr[self.row+2][self.lExt+i] = "B"
								self.arr[self.row][self.lExt+i] = " "
								self.arr[self.row+1][self.lExt+i] = " "
							else:
								self.arr[self.row+3][self.lExt+i] = "B"
								self.arr[self.row+2][self.lExt+i] = "B"
						self.flag = 1
						self.row += 2
		try:
			tty.setcbreak(sys.stdin.fileno())		#this function by defualt calls the while loop 
			while 1:  								#however if an input is not given on time, the enemy moves on its own without waiting for user input
				self.move_enemy()
					
				if self.check == 0:
					boom()	        
				if isData():	
					ch = sys.stdin.read(1)
					if ch == 'q':
						exit(1)
					if ch == 'b':
						self.flag = drop_bomb(self.arr,self.row,self.lExt,self.rExt,self.flag)
						bombRow = self.row
						bombLt = self.lExt
						bombRt = self.rExt
						self.check = 0
						self.count = 0
					if(ch == 'd'):
						move_right()
					if(ch == 'a'):
						move_left()
					if ch == 'w':
						move_up()
					if ch == 's':
						move_down()	
				time.sleep(0.5)
				
		finally:
			pass 


	
		
						




					




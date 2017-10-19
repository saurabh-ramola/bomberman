from __future__ import print_function
from board import *
from person import *
from random import *
import time

class Enemy(Board,man):
	
	def __init__(self):
		Board.__init__(self)
		man.__init__(self)
		self.num_enemy = 4
		self.type = 1
		
	def initial(self):						#defining the initial coordinates of the enemies
		self.r = [8,4,18,18]				
		self.lt = [2,58,58,42]
		self.rt = [5,61,61,45]
		self.score = 0
	def remove_enemy(self,j):				#function to remove enemy when it gets destroyed by a bomb
		for i in range(0,4):
			self.arr[self.r[j]][self.lt[j]+i] = " "
			self.arr[self.r[j]+1][self.lt[j]+i] = " "
		self.r[j] = -1						#corresponding coordinates made zero so that we can keep track of it
		self.rt[j] = -1
		self.lt[j] = -1

	def move_enemy(self):					#main function to move the enemies in random manner
		def checkEnemy():
			for i in range(0,4):
				if self.r[i] == 0:
					self.num_enemy-=1
	
		move = randint(1,4)
		for j in range(0,4):				#crating the enemies at their initial positions
			for i in range(0,4):
				self.arr[self.r[j]][self.lt[j]+i] = "E"
				self.arr[self.r[j]+1][self.lt[j]+i] = "E"
		flag = 0							#flag is used to keep track of random movements and resolve conflicts when there are no places to go
		while flag!=1:
			#print(move)
			if self.score == 400:
				print("YOU WIN\n")
				print("YOUR SCORE IS \t")
				print(self.score)
				exit(1)
			if move == 1:
				for j in range(0,4):		#checking the conditions for the enemies to move left within the rules of the game
					if self.lt[j] >= 6 and self.arr[self.r[j]][self.lt[j]-4] != "X" and self.arr[self.r[j]][self.lt[j]-4] != "E" and self.r[j]!= -1:
						if self.arr[self.r[j]][self.lt[j]-1] == 'B':
							for i in range(1,5):
								self.arr[self.r[j]][self.lt[j]-i] = "E"
								self.arr[self.r[j]][self.rt[j]] = " "
								self.arr[self.r[j]+1][self.lt[j]-i] = "E"
								self.arr[self.r[j]+1][self.rt[j]] = " "
								self.rt[j]-=1
							self.dispBoard()
							print("YOU ARE DEAD")
							print('\n')
							print(self.score)
							exit(1)
						elif self.arr[self.r[j]][self.lt[j]-5] in range(0,2):	#keeping track of the enemies killed and simultaneously updating the scores
							self.remove_enemy(j)
							self.score+=100
							self.dispBoard()
							print("Your score is: \t")
							print(self.score)
						else:
							for i in range(1,5):
								self.arr[self.r[j]][self.lt[j]-i] = "E"
								self.arr[self.r[j]][self.rt[j]] = " "
								self.arr[self.r[j]+1][self.lt[j]-i] = "E"
								self.arr[self.r[j]+1][self.rt[j]] = " "
								self.rt[j] -= 1
							self.lt[j] -= 4
							flag = 1 
							self.dispBoard()	
							print("Your score is: \t")
							print(self.score)   
					else:
						move = 2
			if move == 2: #checking the conditions for the enemies to move right within the rules of the game
				for j in range(0,4):
					if self.lt[j] < 56 and self.arr[self.r[j]][self.rt[j]+4] != "X" and self.arr[self.r[j]][self.rt[j]+4] != "E" and self.r[j]!= -1:
						if self.arr[self.r[j]][self.rt[j]+1] == 'B':
							for i in range(1,5):
								self.arr[self.r[j]][self.rt[j]+i] == 'E'
								self.arr[self.r[j]+1][self.rt[j]+i] == 'E'
								self.arr[self.r[j]][self.lt[j]] = " "
								self.arr[self.r[j]+1][self.lt[j]] = " "
								self.lt[j] += 1
							self.dispBoard()
							print("YOU ARE DEAD")
							print('\n')
							print(self.score)
							
							exit(1)
						elif self.arr[self.r[j]][self.rt[j]+5] in range (0,2): #keeping track of the enemies killed and simultaneously updating the scores
							self.remove_enemy(j)
							self.score+=100
							self.dispBoard()
							print("Your score is: \t")
							print(self.score)
						else:
							for i in range(1,5):
								self.arr[self.r[j]][self.rt[j]+i] = "E"
								self.arr[self.r[j]][self.lt[j]] = " "
								self.arr[self.r[j]+1][self.rt[j]+i] = "E"
								self.arr[self.r[j]+1][self.lt[j]] = " "
								self.lt[j] += 1
							self.rt[j] += 4
							flag = 1
							self.dispBoard()
							print("Your score is: \t")
							print(self.score)
					else:	
						move = 3
			if move == 3: #checking the conditions for the enemies to move up within the rules of the game
				for j in range(0,4):
					if self.r[j] > 2 and self.arr[self.r[j]-2][self.lt[j]] != "X" and self.arr[self.r[j]-2][self.lt[j]] != "E" and self.r[j]!= -1:
						if self.arr[self.r[j]-1][self.lt[j]] == 'B':
							for i in range(0,4):
								self.arr[self.r[j]-2][self.lt[j]+i] = "E"
								self.arr[self.r[j]-1][self.lt[j]+i] = "E"
								self.arr[self.r[j]+1][self.lt[j]+i] = " "
								self.arr[self.r[j]][self.lt[j]+i] = " "
							self.dispBoard()
							print("YOU ARE DEAD")
							print('\n')
							print(self.score)
							exit(1)
						elif self.arr[self.r[j]-3][self.lt[j]] in range(0,2):
							self.remove_enemy(j)
							self.score+=100
							self.dispBoard()
							print("Your score is: \t")
							print(self.score)
						else:
							for i in range(0,4):
								self.arr[self.r[j]-2][self.lt[j]+i] = "E"
								self.arr[self.r[j]-1][self.lt[j]+i] = "E"
								self.arr[self.r[j]+1][self.lt[j]+i] = " "
								self.arr[self.r[j]][self.lt[j]+i] = " "
							self.r[j] -= 2  
							flag = 1 
							self.dispBoard() 
							print("Your score is: \t")
							print(self.score)
					else:	
						move = 4		
			if move == 4:#checking the conditions for the enemies to move down within the rules of the game
				for j in range(0,4):
					if self.r[j] + 2 < 19 and self.arr[self.r[j]+2][self.lt[j]] != "X" and self.arr[self.r[j]+2][self.lt[j]] != "E" and self.r[j]!= -1:
						if self.arr[self.r[j]+2][self.lt[j]] == 'B':
							for i in range(0,4):
								self.arr[self.r[j]+3][self.lt[j]+i] = "E"
								self.arr[self.r[j]+2][self.lt[j]+i] = "E"
								self.arr[self.r[j]][self.lt[j]+i] = " "
								self.arr[self.r[j]+1][self.lt[j]+i] = " "
							self.dispBoard()
							print("YOU ARE DEAD")
							print('\n')
							print(self.score)
							#print('\n')
							exit(1)
						elif self.arr[self.r[j]+4][self.lt[j]] in range(0,2):
							self.remove_enemy(j)
							self.score+=100
							self.dispBoard()
							print("Your score is: \t")
							print(self.score)
						else:
							for i in range(0,4):
								self.arr[self.r[j]+3][self.lt[j]+i] = "E"
								self.arr[self.r[j]+2][self.lt[j]+i] = "E"
								self.arr[self.r[j]][self.lt[j]+i] = " "
								self.arr[self.r[j]+1][self.lt[j]+i] = " "
							self.r[j] += 2
							flag = 1
							self.dispBoard()
							print("Your score is: \t")
							print(self.score)
					else:	
						move = 1

				
				





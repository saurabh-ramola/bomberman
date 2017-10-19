from person import *
from main import *	
b = Main()		#creating a main object
b.initialPos()	#calling the function to create initial display configuration	
b.move_man()	#calling the driver function which takes care of all aspects of the game -> moving bMan,enemies,bombs and deaths

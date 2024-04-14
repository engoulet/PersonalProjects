import random
from Battleship.Ship import Ship

def is_integer(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()



def proper_coords(input):
	inp = input

	if inp == "": #no input
		return False

	format_count = 0 #counts the number of vital input components, such as the comma. 
	#loop to find at least one int before first comma
	for ch in inp:
		if is_integer(ch) and format_count < 1:
			format_count = 1
		elif ch == "," and format_count < 1:
			return False
		elif ch == ",":
			break
		elif not is_integer(ch):
			return False

	#check that there's one comma between two integers
	for ch in inp:
		if ch == "," and format_count == 1:
			format_count = 2
		elif not is_integer(ch):
			return False

	if format_count < 2: #didn't meet requirements
		return False

	#make sure theres at least one int after the comma
	inp = inp.split(",")
	if len(inp) < 2:
		return False
	elif not is_integer(inp[1]):
		return False

	return True


class Board():
	def __init__(self):
		self.board = []
		temp_list = [] #used to constrcut board
		
		#add top row
		for i in range(0, 12):
			temp_list.append("*")
		self.board.append(temp_list)


		#add middle rows where pieces will be
		for j in range(0, 12 - 2):
			temp_list = []
			for i in range(0, 12):
				if i == 0 or i == (12 - 1): #edge of row
					temp_list.append("*")
				else:
					temp_list.append(" ")
			self.board.append(temp_list)

		
		temp_list = []
		#add last row
		for i in range(0, 12):
			temp_list.append("*")
		self.board.append(temp_list)


	def fire(self, x, y):
		#returns 0 if HIT, 1 if MISS, and 2 if INVALID
		if self.board[12 - y - 1][x] == "@":
			hit = True
			self.board[12 - y - 1][x] = "X"
			return 0

		elif self.board[12 - y - 1][x] == " ":
			self.board[12 - y - 1][x] = "O"
			return 1
			
		else:
			return 2


	def print_board(self):
		print()
		i = 11
		for ele in self.board:
			line = ''
			for item in ele:
				line = line + ' ' + item
			
			if not i == 11 and not i == 0:
				line = str(i) + line
			else:
				line = " " + line
			if not i == 10:
				line = " " + line
			print(line)
			i = i - 1
		print("     1 2 3 4 5 6 7 8 9 10")


	


	def make_ship(self, ship_size, randomize):

		if not randomize: #ask user for input if not randomize
			valid = False #tracks if the user has given a valid set of coordinates
			while not valid:
				valid = True
				#take input for where home ships are
				length = 0
				#this loops until the user gives a ship with the right length
				while not length == ship_size:
					print("Where would you like your " + str(ship_size) + " long ship?")
					print("q: quit")
					ship_inp = []
					ship_inp = input("> ")

					if ship_inp == "q": #user said to quit
						return "q"

					#check format
					space = False #checks that there's at least one space
					for ch in ship_inp:
						if ch == " ":
							space = True

					if space:
						ship_inp = ship_inp.split()
						if len(ship_inp) == 2:
							if not proper_coords(ship_inp[0]) or not proper_coords(ship_inp[1]):
								print("Improper format!")
								continue 
						else:
							print("Improper format!")
							continue 
					else:
						print("Improper format!")
						continue 


					ships = [] #holds home ship coords
					#split the two coords into an array
					for coord in ship_inp:
						temp = coord.split(",")
						for i in range(0, len(temp)):
							temp[i] = int(temp[i])
						ships.append(temp)

					#check if coords are out of bounds
					OOB = False #out of bounds
					for coord in ships:
						for i in coord:
							if i > 10 or i < 1:
								OOB = True
					if OOB:
						print("Ship out of bounds!")
						continue

					#makes sure the ship is the right size
					length = 0
					if ships[0][0] == ships[1][0]:
						length = abs(ships[0][1] - ships[1][1]) + 1
					else:
						length = abs(ships[0][0] - ships[1][0]) + 1

					if not length == ship_size:
						print("Wrong length of ship!")


				final_coords = []
				ship_creation_coords = [] #stores the coords that will be used when making a new ship object
				#this if statement finds the orientation of the given ship
				if ships[0][0] == ships[1][0]:
					start = max(ships[0][1], ships[1][1]) #the starting coordinate for drawing the ship

					for i in range(0, length): #add ship coords to final_coords
						if self.board[12 - (start - i) - 1][ships[0][0]] == "@":
							print("This would cause a ship overlap!")
							valid = False
							break
						final_coords.append([12 - (start - i) - 1, ships[0][0]])
						ship_creation_coords.append([ships[0][0], start - i])
				else:
					start = min(ships[0][0], ships[1][0]) #the starting coordinate for drawing the ship

					for i in range(0, length): #add ship coords to final_coords
						if self.board[12 - ships[0][1] - 1][start + i] == "@":
							print("This would cause a ship overlap!")
							valid = False
							break
						final_coords.append([12 - ships[0][1] - 1, start + i])
						ship_creation_coords.append([start + i, ships[0][1]])

				if valid:
					#draw ship
					for coord in final_coords:
						self.board[coord[0]][coord[1]] = "@"
					return Ship(ship_creation_coords, ship_size)


		else:

			valid = False
			while not valid:
				valid = True
				x_or_y = random.randint(0, 1) #0 = x and 1 = y - used to determine orientation of ship
				ships = [[0, 0], [0, 0]]
				if x_or_y == 0:
					ships[0][0] = random.randint(1,10)
					ships[1][0] = ships[0][0]
					ships[0][1] = random.randint(1,10)
					ships[1][1] = ships[0][1] + ship_size - 1 #try to extend ship upwards first, downwards otherwise
					if ships[1][1] > 10:
						ships[1][1] = ships[0][1] - ship_size + 1

				else:
					ships[0][1] = random.randint(1,10)
					ships[1][1] = ships[0][1]
					ships[0][0] = random.randint(1,10)
					ships[1][0] = ships[0][0] + ship_size - 1 #try to extend ship rightwards first, leftwards otherwise
					if ships[1][0] > 10:
						ships[1][0] = ships[0][0] - ship_size + 1


				final_coords = []
				ship_creation_coords = [] #stores the coords that will be used when making a new ship object
				#this if statement finds the orientation of the given ship
				if ships[0][0] == ships[1][0]:
					start = max(ships[0][1], ships[1][1]) #the starting coordinate for drawing the ship

					for i in range(0, ship_size): #add ship coords to final_coords
						if self.board[12 - (start - i) - 1][ships[0][0]] == "@":
							valid = False
							break
						final_coords.append([12 - (start - i) - 1, ships[0][0]])
						ship_creation_coords.append([ships[0][0], start - i])
				else:
					start = min(ships[0][0], ships[1][0]) #the starting coordinate for drawing the ship

					for i in range(0, ship_size): #add ship coords to final_coords
						if self.board[12 - ships[0][1] - 1][start + i] == "@":
							valid = False
							break
						final_coords.append([12 - ships[0][1] - 1, start + i])
						ship_creation_coords.append([start + i, ships[0][1]])

				if valid:
					#draw ship
					for coord in final_coords:
						self.board[coord[0]][coord[1]] = "@"
					return Ship(ship_creation_coords, ship_size)


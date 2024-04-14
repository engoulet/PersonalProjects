import random, time, sys, os

#add parent directory to the system path so sibling modules can be imported
sys.path.insert(0, "\\".join(os.path.realpath(__file__).split("\\")[0:-2]))

from Battleship.Board import Board
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
	

def main():

	end = False
	while not end:
		home = Board()
		enemy = Board() #holds the locations of enemy ships
		ghost = Board() #only shows where you've hit an enemy ship

		home_ships = []
		enemy_ships = []

		home.print_board()


		print("Enter the coords of the two ends of the ship.\nDo so in the following format: 1,2 1,4")
		#add home ships
		home_ships.append(home.make_ship(5, False))
		if "q" in home_ships: #check if user said to quit
			end = True
			break
		home.print_board()
		home_ships.append(home.make_ship(4, False))
		if "q" in home_ships:
			end = True
			break
		home.print_board()
		home_ships.append(home.make_ship(3, False))
		if "q" in home_ships:
			end = True
			break
		home.print_board()
		home_ships.append(home.make_ship(3, False))
		if "q" in home_ships:
			end = True
			break
		home.print_board()
		home_ships.append(home.make_ship(2, False))
		if "q" in home_ships:
			end = True
			break

		

		#add enemy ships
		enemy_ships.append(enemy.make_ship(5, True))
		enemy_ships.append(enemy.make_ship(4, True))
		enemy_ships.append(enemy.make_ship(3, True))
		enemy_ships.append(enemy.make_ship(3, True))
		enemy_ships.append(enemy.make_ship(2, True))

		ghost.print_board()
		home.print_board()

		print("\nEnter moves in the following format: 1,1")
		print("START")

		queued_CPU_moves = []

		game_over = False
		while not game_over:
			#take player input
			inp = []
			print("Your move!")
			print("q: quit")
			inp = input("> ")

			if inp == "q": #check if user said to quit
				end = True
				break

			#check input format
			if not proper_coords(inp):
				print("Improper format!")
				continue


			inp = inp.split(",")
			inp[0] = int(inp[0])
			inp[1] = int(inp[1])
			#check if input is in range
			if inp[0] > 10 or inp[0] < 1 or inp[1] > 10 or inp[1] < 1:
				print("Out of bounds!")
				continue
			H_or_M = enemy.fire(inp[0], inp[1]) #fire
			

			if H_or_M == 0: #hit 
				#update ghost board
				ghost.board[12 - inp[1] - 1][inp[0]] = "X"
				ghost.print_board()
				home.print_board()
				#loop through all ships to see which was hit
				for ship in enemy_ships:
					for coord in ship.coord_set:
						if inp[0] == coord[0] and inp[1] == coord[1]: #ship found
							ship.lose_health()
							if ship.health == 0:
								print("HIT AND SINK")
								enemy_ships.remove(ship)
								if len(enemy_ships) == 0:
									print("GAME OVER!\nYou Win!")
									game_over = True
							else:
								print("HIT")
			elif H_or_M == 1: #miss
				#update ghost board
				ghost.board[12 - inp[1] - 1][inp[0]] = "O"
				ghost.print_board()
				home.print_board()
				print("MISS")
			elif H_or_M == 2: #invalid
				print("You've already fired in that spot.")
				continue
			
			#check if game is over
			if game_over:
				break



			#enemy's turn
			print("Enemy's move!")
			#wait 2 seconds
			cur_time = time.time()
			temp_time = time.time()
			while (temp_time - cur_time) < 3:
				temp_time = time.time()

			valid = False
			while not valid:
				valid = True


				#generate CPU move
				inp = [0, 0]
				if len(queued_CPU_moves) == 0:
					inp[0] = random.randint(1, 10)
					inp[1] = random.randint(1, 10)
				else:
					inp = queued_CPU_moves.pop()
				
				H_or_M = home.fire(inp[0], inp[1]) #fire
				
				if H_or_M == 0: #hit
					ghost.print_board()
					home.print_board()
					#loop through all ships to see which was hit
					for ship in home_ships:
						for coord in ship.coord_set:
							if inp[0] == coord[0] and inp[1] == coord[1]: #ship found
								ship.unhit_coords.remove(coord)
								#reduce health
								ship.lose_health()

								#queue moves
								queued_CPU_moves = ship.unhit_coords.copy()

								if ship.health == 0:
									print("HIT AND SINK")
									home_ships.remove(ship)
									if len(home_ships) == 0:
										print("GAME OVER!\nYou Lose!")
										game_over = True
								else:
									print("HIT")
				elif H_or_M == 1: #miss
					ghost.print_board()
					home.print_board()
					print("MISS")
				elif H_or_M == 2: #invalid
					valid = False

		if not end:
			print("\nWould you like to play again? (Y/N)")
			inp = input("> ").lower()
			
			end = True
			if inp == "y" or inp == "yes":
				end = False

	print("Thanks for playing!")



if __name__ == "__main__": 
	main()
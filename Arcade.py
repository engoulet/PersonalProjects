import Battleship.Battleship as battleship
import MazeGame as mazeGame
import Hangman as hangman
import GoFish.GoFish as goFish

def is_integer(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()

def main():
	game_count = 4
	quit = False #exit arcade if true
	while not quit:
		print("+----------------------------------------------------------+")
		print("|      __      ____     ____      __      _____    ____    |")
		print("|     /  \\    | __ \\   / ___\\    /  \\    |  __ \\  |  __|   |")
		print("|    / /\\ \\   | |_| | | |       / /\\ \\   | |  | | | \\__    |")
		print("|   / ____ \\  |  _ /  | |____  / ____ \\  | |__| | | /__    |")
		print("|  /_/    \\_\\ |_| \\_\\  \\____/ /_/    \\_\\ |_____/  |____|   |")
		print("|__________________________________________________________|")
		print("|                                                          |")
		print("|    0: Quit                                               |")
		print("|    1: Battleship                                         |")
		print("|    2: Maze Game                                          |")
		print("|    3: Hangman                                            |")
		print("|    4: Go Fish!                                           |")
		print("+----------------------------------------------------------+")
		valid = False
		while not valid:
			inp = input("> ")
			#check input is valid
			if is_integer(inp):
				if int(inp) >= 0 and int(inp) <= game_count:
					valid = True
				else:
					print("Invalid Input!")
			else:
				print("Invalid Input!")

		if not quit:
			if inp == "0":
				quit = True
			elif inp == "1":
				battleship.main()
			elif inp == "2":
				mazeGame.main()
			elif inp == "3":
				hangman.main()
			elif inp == "4":
				goFish.main()

		

	print("Thanks for coming!")


main()
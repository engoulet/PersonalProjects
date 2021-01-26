import Battleship
import maze_game_release
import hangman

def is_integer(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()

def main():
	game_count = 3
	print("Welcome to Eric's Arcade!\nSelect a game you'd like to play:")
	quit = False #exit arcade if true
	while not quit:
		print("0. Quit\n1. Battleship\n2. Maze Game\n3. Hangman")
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
				Battleship.main()
			elif inp == "2":
				maze_game_release.main()
			elif inp == "3":
				hangman.main()

		

	print("Thanks for coming!")


main()
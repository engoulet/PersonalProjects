import random, time, sys

def main():
	endOfSession = False
	while not endOfSession:
		#initialize game and ask how many opponents to face
		opponents, names = initGame()
		
		cardsDrawn = {}  #tracks what cards can no longer be drawn
		hands = [[]]  #stores all player hands
		completeSets = [[]] #stores the completed sets of cards as players gather them
		
		#add opponents hands
		for i in range(0, opponents):
			hands.append([])
			completeSets.append([])

		#deal 7 cards to each player
		for i in range(0, 7):
			for hand in hands:
				hand.append(drawCard(cardsDrawn))

		#check for complete sets
		for i, hand in enumerate(hands):
			checkForSets(hand, i, completeSets, names)

		#begin play
		gameOver = False
		currentTurn = 0  #tracks which player's turn it is
		botTurnTime = 5
		playerCanStillPlay = True
		
		while not gameOver:
			printHands(hands, completeSets, names)

			#check for empty hand
			if len(hands[currentTurn]) == 0:
				print("%s's hand is empty. Drawing one card automatically\n" % (names[currentTurn]))
				newCard = drawCard(cardsDrawn)
				if newCard == -1: 
					print("The deck is empty, %s's turn is skipped..." % (names[currentTurn]))
					if currentTurn == 0 and playerCanStillPlay:
						print("\n\n\nYou can no longer play. In a few seconds, the remainder of the game will be sped up.\n\n")
						waitSeconds(10)
						botTurnTime = 1
						playerCanStillPlay = False

					currentTurn = (currentTurn + 1) % (opponents + 1)
					continue
				else:
					hands[currentTurn].append(newCard)
					#tell player what they drew
					if currentTurn == 0:
						print("%s drew the %s" % (names[currentTurn], displayCard(newCard)))

				printHands(hands, completeSets, names)

			#take input from either the player or the bot

			if currentTurn == 0:  #player's turn
				print("What card would you like to ask for, and from whom? \n(Format: Card-Player  |  Ex: A-1  --> requests Ace's from player 1)")
				
				validInp = False
				while not validInp:
					inp = str.capitalize(input(">>>  "))
	
					#check for proper input
					if proper_input(inp, hands[currentTurn], opponents):
						validInp = True

			else:  #bot's turn
				#wait a few seconds
				waitSeconds(botTurnTime)

				#select a number and player
				num = evalNum(hands[currentTurn][random.randint(0, len(hands[currentTurn]) - 1)])
				player = random.randint(0, opponents)
				while player == currentTurn or len(hands[player]) == 0:
					player = random.randint(0, opponents)


				inp = "%s-%d" % (num, player)



			#eval input and collect the cards
			inp = inp.split("-")
			inp[1] = int(inp[1])
			cardsStolen = collectCardsFromOpp(hands, inp[0], inp[1], currentTurn)
			
			print("%s asks for %s's from %s..." % (names[currentTurn], inp[0], names[inp[1]]))
			if cardsStolen == 0:
				newCard = drawCard(cardsDrawn)
				if newCard == -1:
					print("Go Fish!\nThe deck is empty, %s cannot draw a card..." % (names[currentTurn]))
				else:
					print("Go Fish!\nDrawing a new card into %s's hand..." % (names[currentTurn]))
					hands[currentTurn].append(newCard)
					#tell player what they drew
					if currentTurn == 0:
						print("%s drew the %s" % (names[currentTurn], displayCard(newCard)))
			else:
				tense = "them"
				if cardsStolen == 1: tense = "it"

				print("%s has %d and gives %s to %s" % (names[inp[1]], cardsStolen, tense, names[currentTurn]))

			
			#check if player completed any sets of cards
			checkForSets(hands[currentTurn], currentTurn, completeSets, names)

			#check if game over
			for i, hand in enumerate(hands):
				if len(hand) != 0:
					break
				if i == len(hands) - 1 and len(cardsDrawn) == 52: 
					#reached end of list (all players have no cards) and deck is empty
					gameOver = True
				
			currentTurn = (currentTurn + 1) % (opponents + 1)

		printHands(hands, completeSets, names)
		decideWinner(completeSets, names)

		print("Would you like to play again?")
		valid = False
		while not valid:
			inp = input(">>>  ")
			if inp == "Y" or inp == "y":
				endOfSession = False
				valid = True
			elif inp == "N" or inp == "n":
				endOfSession = True
				valid = True
			else:
				print("Invalid input!")
	

def initGame():
	print("Welcome to Go Fish!\n")
	while True:
		opponents = input("How many opponents would you like to face? (1 - 6)\n>>>  ")
		if opponents.isdigit(): 
			opponents = int(opponents)
			if opponents >= 1 and opponents <= 6:
				nameList = ["Joe", "Randy", "Cole", "Sarah", "Tony", "Regenald", "Tim", "Frank", "Betty", "Penny", "Jenny", "Kate", "Hannah", "Barry", "Sally"]

				names = []
				names.append(input("What would you like your name to be?\n>>>  "))
			
				for i in range(0, opponents):
					names.append(nameList.pop(random.randint(0, len(nameList) - 1)))
			
				return opponents, names
			else: 
				print("Invalid input!")
		else:
			print("Invalid input!")

def decideWinner(completeSets, names):
	print("Game Over!")
	max = 0
	winners = None
	#determine who the winner(s) are
	for i, hand in enumerate(completeSets):
		if len(hand) > max:
			max = len(hand)
			winners = []
			winners.append(names[i])
		elif len(hand) == max:
			winners.append(names[i])
			
	#if it's a tie
	if len(winners) > 1:
		for i, winner in enumerate(winners):
			if i == len(winners) - 1:
				sys.stdout.write("and %s tied for 1st place!!!\n\n" % (winner))
			else:
				sys.stdout.write("%s, " % (winner))
	else: #if someone won
		print(winners[0] + " wins!!!\n")


#checks for complete sets of cards for a player
def checkForSets(hand, player, completeSets, names):
	counter = {}
	cardsToRemove = {}

	#count the cards of each number and add them to the complete sets
	for card in hand:
		cardNum = evalNum(card)

		if cardNum not in counter:
			counter[cardNum] = 1
		else:
			counter[cardNum] += 1
			if counter[cardNum] == 4:
				completeSets[player].append(cardNum)
				cardsToRemove[cardNum] = True
				print("\n%s completed the set of %s's\n" % (names[player], cardNum))
	
	#remove the cards that have become complete sets from the player's hand
	i = 0
	while i < len(hand):
		if cardsToRemove.get(evalNum(hand[i])):
			hand.pop(i)
		else:
			i += 1


#wait for a number of seconds
def waitSeconds(secs):
	cur_time = time.time()
	temp_time = time.time()
	while (temp_time - cur_time) < secs:
		temp_time = time.time()

#takes the card ID number (1 - 52) and returns it in a nicer format (5'S for 5 of spades or K'D for king of diamonds)
def displayCard(id):
	num = evalNum(id)
	suit = evalSuit(id)

	return "%s'%s" % (num, suit)


#takes an id and returns its corresponding card number
def evalNum(id):
	num = id % 13
	if num == 1: num = "A"
	elif num == 11: num = "J"
	elif num == 12: num = "Q"
	elif num == 0: num = "K"
	else: num = str(num)

	return num


#takes an id and returns its corresponding suit
def evalSuit(id):
	temp = int(id / 13)
	if temp == 0: suit = "D"
	elif temp == 1: suit = "S"
	elif temp == 2: suit = "C"
	else: suit = "H"

	return suit


#takes a card ID number (1 - 52) and checks if it matches the provided card number (0 - 12)
def compareCard(num, id):
	if num == "A" and id % 13 == 1: return True
	elif num == "J" and id % 13 == 11: return True
	elif num == "Q" and id % 13 == 12: return True
	elif num == "K" and id % 13 == 0: return True
	elif num.isdigit() and int(num) == id % 13: return True
	else: return False 


#collects all cards that match the number of the "num" param (0 - 12) from the target player and give them to the destination player (dest)
#returns how many cards were collected
def collectCardsFromOpp(hands, num, target, dest):
	count = 0  #count how many card are found

	#loop through the hand of the target player
	i = 0
	while i < len(hands[target]):
		if compareCard(num, hands[target][i]):  #if the card matches the desired number, take it
			hands[dest].append(hands[target].pop(i))
			count = count + 1
		else:
			i += 1

	return count


def drawCard(cardsDrawn):
	if len(cardsDrawn) >= 52:
		return -1
	
	card = random.randint(1,52)

	while cardsDrawn.get(card) == True:
		card = random.randint(1,52)

	cardsDrawn[card] = True
	return card


def printHands(hands, completedSets, names):
	debug = False  #true if verbose player hands is enabled
	print()
	for i, hand in enumerate(hands):
		#sort the hand
		temp = []
		for card in hand:
			temp.append(displayCard(card))
		temp = sorted(temp)

		#print the hand
		sys.stdout.write("Player %d (%s):\n[  " % (i, names[i]))
		for card in temp:
			if (i == 0) or (i != 0 and debug):
				sys.stdout.write(card + "  ")
			else:
				sys.stdout.write("***  ")
		sys.stdout.write("]    [  ")
		for number in completedSets[i]:
			sys.stdout.write(number + "  ")
		sys.stdout.write("]\n\n")


def proper_input(inp, hand, opponents):
	#check for correct length
	if len(inp) > 4 or len(inp) < 3:
		print("Invalid input format!")
		return False
	
	#check that if it's length 4, the first half is valid
	if len(inp) == 4 and inp[0:2] != "10":
		print("Invalid input format!")
		return False
	
	#check that if it's length 3, and it's not a valid character or it's an invalid character, return false
	if len(inp) == 3 and ((not inp[0].isdigit() and inp[0] != "A" and inp[0] != "J" and inp[0] != "Q" and inp[0] != "K") 
		       									or inp[0] == "1" or inp[0] == "0"):
		print("Invalid input format!")
		return False

	#check for the hyphen
	if inp[-2] != "-":
		print("Invalid input format!")
		return False

	#check that the second half is correct
	if inp[-1].isdigit() and (int(inp[-1]) < 1 or int(inp[-1]) > opponents):
		print("Invalid input format!")
		return False
	
	#formatting is correct, now check if the action is valid
	for card in hand:
		if compareCard(inp.split("-")[0], card):
			return True 

	print("Invalid input! You don't have the card you asked for")
	return False



if __name__ == "__main__":
	main()


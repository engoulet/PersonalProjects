import random, time, sys, os, copy

#add parent directory to the system path so sibling modules can be imported
sys.path.insert(0, "\\".join(os.path.realpath(__file__).split("\\")[0:-2]))

from GoFish.GoFishPlayer import Player
from Utils.Deck import Deck



debug = False  #true if verbose player hands is enabled

def main():
	endOfSession = False
	while not endOfSession:
		#initialize game and ask how many opponents to face and at what difficulty
		players = initGame()
		
		deck = Deck()  #tracks the deck of cards

		#deal 7 cards to each player
		for i in range(0, 7):
			for j, player in enumerate(players):
				newCard = deck.drawCard(True) if (j == 0 or debug) else deck.drawCard(False)
				player.hand.append(newCard)

		#check for complete sets
		for player in players:
			checkForSets(player)

		#begin play
		gameOver = False
		currentTurn = 0  #tracks which player's turn it is
		botTurnTime = 5  #number of seconds in between each bot's turn
		playerCanStillPlay = True  #set to false once the player can no longer draw or play any cards
		
		while not gameOver:

			#check for empty hand
			if len(players[currentTurn].hand) == 0:
				print("%s's hand is empty. Drawing one card automatically\n" % (players[currentTurn].name))
				newCard = deck.drawCard(True) if (currentTurn == 0 or debug) else deck.drawCard(False)
				if newCard == None: 
					print("The deck is empty, %s's turn is skipped...\n" % (players[currentTurn].name))
					if currentTurn == 0 and playerCanStillPlay:
						print("\n\n\nYou can no longer play. In a few seconds, the remainder of the game will be sped up.\n\n")
						waitSeconds(10)
						botTurnTime = 1
						playerCanStillPlay = False

					currentTurn = (currentTurn + 1) % len(players)
					continue
				else:
					players[currentTurn].hand.append(newCard)
					#tell player what they drew
					if currentTurn == 0:
						print("%s drew the %s" % (players[currentTurn].name, newCard.displayCard()))


			if currentTurn == 0: printHands(players)

			#take input from either the player or the bot

			if currentTurn == 0:  #player's turn
				print("What card would you like to ask for, and from whom? \n(Format: Card-Player  |  Ex: A-1  --> requests Ace's from player 1)\n(type \"quit\" to quit)")
				
				validInp = False
				while not validInp:
					inp = str.upper(input(">>>  "))

					if (inp == "QUIT"):
						return

					#check for proper input
					if proper_input(inp, players, currentTurn):
							validInp = True


			else:  #bot's turn

				#select a number and player
				inp = generateMoveForPlayer(players, currentTurn)


			#eval input and collect the cards
			inp = inp.split("-")
			inp[1] = int(inp[1])
			cardsStolen = collectCardsFromOpp(inp, players, currentTurn)

			players[currentTurn].setLastAskedFor(inp[0]) #update last asked for
			
			print("%s asks for %s's from %s..." % (players[currentTurn].name, inp[0], players[inp[1]].name))
			if cardsStolen == 0:
				newCard = deck.drawCard(True) if (currentTurn == 0 or debug) else deck.drawCard(False)
				if newCard == None:
					print("Go Fish!\nThe deck is empty, %s cannot draw a card..." % (players[currentTurn].name))
				else:
					print("Go Fish!\nDrawing a new card into %s's hand..." % (players[currentTurn].name))
					players[currentTurn].hand.append(newCard)
					#tell player what they drew
					if currentTurn == 0:
						print("%s drew the %s" % (players[currentTurn].name, newCard.displayCard()))
			else:
				tense = "them"
				if cardsStolen == 1: tense = "it"

				print("%s has %d and gives %s to %s" % (players[inp[1]].name, cardsStolen, tense, players[currentTurn].name))
			print("\n")

			
			#check if player completed any sets of cards
			checkForSets(players[currentTurn])

			print("--------------------------------")

			#wait a few seconds
			waitSeconds(botTurnTime)

			#check if game over
			for i, player in enumerate(players):
				if len(player.hand) != 0:
					break
				if i == len(players) - 1 and len(deck.cardsDrawn) == 52: 
					#reached end of list (all players have no cards) and deck is empty
					gameOver = True
				
			currentTurn = (currentTurn + 1) % len(players)

		printHands(players)
		decideWinner(players)

		print("Would you like to play again? (Y/N)")
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
	
	difficulty = None
	while True:
		print("What difficulty would you like to play on?")
		print("1 : Easy (Players make random moves)")
		print("2 : Normal (Players remember others' most recent move and have randomized skill levels)")
		print("3 : Hard (Players remember others' most recent move and have a high skill level)")
		difficulty = input(">>>  ")
		if difficulty.isdigit(): 
			difficulty = int(difficulty)
			if difficulty >= 1 and difficulty <= 3:
				break
			else: 
				print("Invalid input!")
		else:
			print("Invalid input!")

	players = []
	while True:
		opponents = input("\nHow many opponents would you like to face? (1 - 6)\n>>>  ")
		if opponents.isdigit(): 
			opponents = int(opponents)
			if opponents >= 1 and opponents <= 6:
				nameList = ["Joe", "Randy", "Cole", "Sarah", "Tony", "Regenald", "Tim", "Frank", "Betty", "Penny", "Jenny", "Kate", "Hannah", "Barry", "Sally"]

				players.append(Player(input("\nWhat would you like your name to be?\n>>>  "), difficulty))
			
				for i in range(0, opponents):
					players.append(Player(nameList.pop(random.randint(0, len(nameList) - 1)), difficulty))
			
				return players
			else: 
				print("Invalid input!")
		else:
			print("Invalid input!")


def decideWinner(players):
	print("Game Over!")
	max = -1
	winners = None
	#determine who the winner(s) are
	for player in players:
		if len(player.completeSets) > max:
			max = len(player.completeSets)
			winners = []
			winners.append(player.name)
		elif len(player.completeSets) == max:
			winners.append(player.name)
			
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
def checkForSets(player):
	counter = {}
	cardsToRemove = {}

	#count the cards of each number and add them to the complete sets
	for card in player.hand:
		cardNum = card.evalNum()

		if cardNum not in counter:
			counter[cardNum] = 1
		else:
			counter[cardNum] += 1
			if counter[cardNum] == 4:
				player.completeSets.append(cardNum)
				cardsToRemove[cardNum] = True
				print("%s completed the set of %s's\n\n" % (player.name, cardNum))
	
	#remove the cards that have become complete sets from the player's hand
	i = 0
	while i < len(player.hand):
		if cardsToRemove.get(player.hand[i].evalNum()):
			player.hand.pop(i)
		else:
			i += 1


#wait for a number of seconds
def waitSeconds(secs):
	cur_time = time.time()
	temp_time = time.time()
	while (temp_time - cur_time) < secs:
		temp_time = time.time()


#collects all cards that match the given card number (0 - 12) from the target player and give them to the player whose turn it is
#returns how many cards were collected
def collectCardsFromOpp(inp, players, currentTurn):
	count = 0  #count how many card are found
	target = players[inp[1]]
	dest = players[currentTurn]
	num = inp[0]  #desired card number

	#loop through the hand of the target player
	i = 0
	while i < len(target.hand):
		if target.hand[i].hasValueOf(num):  #if the card matches the desired number, take it
			card = target.hand.pop(i)

			#flip cards accordingly, depending on whos hand they're going to
			if currentTurn == 0:
				card.setFaceup(True)
			else:
				card.setFaceup(False)

			dest.hand.append(card)
			count = count + 1
		else:
			i += 1

	return count


def printHands(players):
	print()
	for i, player in enumerate(players):
		#sort the hand
		temp = []
		for card in player.hand:
			temp.append(card.displayCard())
		temp = sorted(temp)

		#print the hand
		sys.stdout.write("Player %d (%s):\n[  " % (i, player.name))
		for card in temp:
			sys.stdout.write(card + "  ")
	
		#print complete sets
		sys.stdout.write("]           [[  ")
		for number in player.completeSets:
			sys.stdout.write(number + "  ")

		sys.stdout.write("]]\n\n")


def proper_input(inp, players, currentTurn):
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
	if not inp[-1].isdigit() or (int(inp[-1]) < 1 or int(inp[-1]) > len(players) - 1):
		print("Invalid input format!")
		return False

	#check that the target has at least one card
	if len(players[int(inp[-1])].hand) == 0:
		print("Invalid input! Your target has no cards")
		return False
	
	#formatting is correct, now check if the action is valid
	for card in players[currentTurn].hand:
		if card.hasValueOf(inp.split("-")[0]):
			return True 

	print("Invalid input! You don't have the card you asked for")
	return False

#generates a move for the requested player. The skillfulness of the move is determined by the difficulty
def generateMoveForPlayer(players, currentTurn):
	player = players[currentTurn]

	targetCard = ""
	targetPlayer = -1
	if player.movePriority == None:
		#Easy

		#select a random card number and random player
		targetCard = players[currentTurn].hand[random.randint(0, len(players[currentTurn].hand) - 1)].evalNum()
		targetPlayer = findRandomPlayerToStealFrom(players, currentTurn)
		return "%s-%d" % (targetCard, targetPlayer)

	else:
		#Normal or Hard

		setsOfThree = []
		setsOfTwo = []
		setsOfOne = []

		#count cards and fill sets
		cardCounts = {}
		for card in player.hand:
			cardNum = card.evalNum()

			if cardNum not in cardCounts:
				cardCounts[cardNum] = 1
			else:
				cardCounts[cardNum] += 1

		for cardNum in cardCounts.keys():
			if cardCounts[cardNum] == 3: 
				setsOfThree.append(cardNum)
			elif cardCounts[cardNum] == 2: 
				setsOfTwo.append(cardNum)
			else: 
				setsOfOne.append(cardNum)

		#randomize the sets to ensure no bias within each set
		setsOfThree = randomizeList(setsOfThree)
		setsOfTwo = randomizeList(setsOfTwo)
		setsOfOne = randomizeList(setsOfOne)

		#select a player and card number based on move priority
		for move in player.movePriority:
			#ask for a card from sets of 3 that another player recently asked for 
			if move == 1 and len(setsOfThree) > 0:
				for targetCard in setsOfThree:
					targetPlayer = findBestPlayerToStealFrom(players, currentTurn, targetCard)
					if targetPlayer != -1: 
						return "%s-%d" % (targetCard, targetPlayer)
			#ask for a card from sets of 2 that another player recently asked for 
			elif move == 2 and len(setsOfTwo) > 0:
				for targetCard in setsOfTwo:
					targetPlayer = findBestPlayerToStealFrom(players, currentTurn, targetCard)
					if targetPlayer != -1: 
						return "%s-%d" % (targetCard, targetPlayer)
			#ask for a card from sets of 1 that another player recently asked for 
			elif move == 3 and len(setsOfOne) > 0:
				for targetCard in setsOfOne:
					targetPlayer = findBestPlayerToStealFrom(players, currentTurn, targetCard)
					if targetPlayer != -1: 
						return "%s-%d" % (targetCard, targetPlayer)
			#randomly ask for a card from setsOfThree
			elif move == 4 and len(setsOfThree) > 0:
				targetCard = setsOfThree[random.randint(0, len(setsOfThree) - 1)]
				targetPlayer = findRandomPlayerToStealFrom(players, currentTurn)
				return "%s-%d" % (targetCard, targetPlayer)
			#randomly ask for a card from setsOfTwo
			elif move == 5 and len(setsOfTwo) > 0:
				targetCard = setsOfTwo[random.randint(0, len(setsOfTwo) - 1)]
				targetPlayer = findRandomPlayerToStealFrom(players, currentTurn)
				return "%s-%d" % (targetCard, targetPlayer)
			#randomly ask for a card from setsOfOne
			elif move == 6 and len(setsOfOne) > 0:
				targetCard = setsOfOne[random.randint(0, len(setsOfOne) - 1)]
				targetPlayer = findRandomPlayerToStealFrom(players, currentTurn)
				return "%s-%d" % (targetCard, targetPlayer)
			


#returns a random player that can be stolen from
def findRandomPlayerToStealFrom(players, currentTurn):
	targetPlayer = random.randint(0, len(players) - 1)

	while targetPlayer == currentTurn or len(players[targetPlayer].hand) == 0:
		targetPlayer = random.randint(0, len(players) - 1)

	return targetPlayer


#tries to find a player that recently asked for the given card, returns random player if none found
def findBestPlayerToStealFrom(players, currentTurn, card):
	#loop backwards from current player to prioritize more recent information
	i = currentTurn - 1
	while i != currentTurn:
		if players[i].getLastAskedFor() == card:
			return i

		i = (i - 1) % len(players)

	return -1

#randomizes a list (non-destructive)
def randomizeList(target):
	temp = copy.deepcopy(target)
	out = []
	while len(temp) > 0: out.append(temp.pop(random.randint(0, len(temp) - 1)))

	return out



if __name__ == "__main__":
	main()


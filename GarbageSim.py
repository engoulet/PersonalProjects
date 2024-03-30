import time, random

def main():
	numSims = int(input("Enter the number of simulated games for each starting card amount\n>>> "))
	
	#run numSims for each starting card amount
	for startingCards in range(10, 0, -1):
		totalDraws = 0		#tracks total draws needed to complete numSims number of games
				

		for i in range(0, numSims):
			#dict to track cards found
			cardsFound = {}
			#dict to track cards already drawn from deck
			cardsDrawn = {}			


			gameOver = False
			while not gameOver:
				#draw card and add to totalDraws
				card = random.randint(1,52)

				while card in cardsDrawn:
					card = random.randint(1,52)

				cardsDrawn[card] = True
				totalDraws = totalDraws + 1

				#print("card drawn: " + str(card) + " (" + str(card%13) + ")")

				#check if found one
				cardValue = card % 13
				if cardValue >= 1 and cardValue <= startingCards:
					#print("---found card: " + str(cardValue))
 
					cardsFound[cardValue] = True

				if len(cardsFound) >= startingCards:
					gameOver = True		

		print("Average number of draws when starting with %d cards: %d\n" % (startingCards, totalDraws/numSims))


		
if __name__ == "__main__": 
	main()


import random, time, sys
from Card import Card

class Deck():

	def __init__(self):
		self.cardsDrawn = {}


	#returns a card object, returns -1 otherwise
	def drawCard(self):
		if len(self.cardsDrawn) >= 52:
			return -1
		
		card = Card()

		while self.cardsDrawn.get(card.getID()) == True:
			card = Card()

		self.cardsDrawn[card.getID()] = True
		return card
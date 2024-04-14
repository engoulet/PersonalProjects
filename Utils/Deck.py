import random, time, sys
from Utils.Card import Card

class Deck():

	def __init__(self):
		self.cardsDrawn = {}

	#returns a card object, returns -1 otherwise
	def drawCard(self, faceup):
		if len(self.cardsDrawn) >= 52:
			return None
		
		card = Card(faceup)

		while self.cardsDrawn.get(card.getID()) == True:
			card = Card(faceup)

		self.cardsDrawn[card.getID()] = True
		return card
import random, time, sys

class Card():

	def __init__(self, faceup):
		self.id = random.randint(1,52)
		self.faceup = faceup

	def getID(self):
		return self.id

	def getFaceup(self):
		return self.faceup

	def setFaceup(self, inp):
		self.faceup = inp

	#takes an id and returns its corresponding card number
	def evalNum(self):
		num = self.id % 13
		if num == 1: num = "A"
		elif num == 11: num = "J"
		elif num == 12: num = "Q"
		elif num == 0: num = "K"
		else: num = str(num)

		return num


	#takes an id and returns its corresponding suit
	def evalSuit(self):
		temp = int(self.id / 13)
		if temp == 0: suit = "D"
		elif temp == 1: suit = "S"
		elif temp == 2: suit = "C"
		else: suit = "H"

		return suit


	#takes the card ID number (1 - 52) and returns it in a nicer format (5~S for 5 of spades or K~D for king of diamonds)
	def displayCard(self):
		if self.faceup: return "%s~%s" % (self.evalNum(), self.evalSuit())
		return "***"


	#takes card ID number (1 - 52) and checks if it matches the provided card number (0 - 12)
	def hasValueOf(self, num):
		if num == "A" and self.id % 13 == 1: return True
		elif num == "J" and self.id % 13 == 11: return True
		elif num == "Q" and self.id % 13 == 12: return True
		elif num == "K" and self.id % 13 == 0: return True
		elif num.isdigit() and int(num) == self.id % 13: return True
		else: return False 
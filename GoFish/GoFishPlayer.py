import random

class Player():

	#Move Priority defines which of the 6 strategic scenarios a bot will prioritize:
	#	1. Bot has a set of 3 and asks for that card from a player that recently asked for it
	#	2. Bot has a set of 2 and asks for that card from a player that recently asked for it
	#	3. Bot has a set of 1 and asks for that card from a player that recently asked for it
	#	4. Bot has a set of 3 and asks for that card from a random player
	#	5. Bot has a set of 2 and asks for that card from a random player
	#	6. Bot has a set of 1 and asks for that card from a random player

	#This priority can be compared to the "skill level" of the bot, with a movePriority of 1,2,3,4,5,6 being most skillful
	def __init__(self, name, difficulty):
		self.name = name
		self.hand = []
		self.completeSets = []
		self.lastAskedFor = None	#only utilized on Normal and Hard difficulty
		
		self.movePriority = [1,2,3,4,5,6] #on Hard, all bots play optimally
		if difficulty == 2:
			temp = [1,2,3,4,5,6]
			self.movePriority = []
			while len(temp) > 0: self.movePriority.append(temp.pop(random.randint(0, len(temp) - 1))) #on Normal, each bot's skill level is random
		elif difficulty == 1:
			self.movePriority = None #on Easy, bots' moves are random


	def getLastAskedFor(self):
		return self.lastAskedFor

	def setLastAskedFor(self, cardNum):
		self.lastAskedFor = cardNum
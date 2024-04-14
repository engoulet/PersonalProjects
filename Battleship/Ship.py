class Ship():

	def __init__(self, coord_set, length):
		self.coord_set = coord_set
		self.unhit_coords = coord_set
		self.length = length
		self.health = length

	def lose_health(self):
		self.health = self.health - 1
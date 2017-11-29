class castle:
	hp = 3
	def __init__(self, name, filename):
		self.name = name
		self.x = xcoor
		self.y = ycoor
		self.image = filename
#		location = random.randrange(100,380)		#Chooses xcoordinate for castle's random location
		castle = pygame.rect(350,250,10,10)		#creates castle rect

	def getHit(self):
		hp -= 1		#if the castle gets hit, it loses 1 HP.  The game is won if the castle is struck 3 times
		return hp
		print("Hit!")

	def resetHP(self):
		hp = 3		#bug testing, in case we need to run it again

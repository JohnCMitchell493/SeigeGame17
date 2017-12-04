import pygame
import math
class Castle(pygame.sprite.Sprite):
	hp = 3
	def __init__(self, name, filename):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
#		self.x = xcoor
#		self.y = ycoor
		self.image = pygame.image.load(filename).convert()
		self.size = self.image.get_size()
		self.image2 = pygame.transform.scale(self.image, (int(self.size[0]*.1), int(self.size[1]*.1)))
		self.rect = self.image2.get_rect()
#		location = random.randrange(100,380)		#Chooses xcoordinate for castle's random location


	def getHit(self):
		hp -= 1		#if the castle gets hit, it loses 1 HP.  The game is won if the castle is struck 3 times
		return hp
		print("Hit!")

	def resetHP(self):
		hp = 3		#bug testing, in case we need to run it again

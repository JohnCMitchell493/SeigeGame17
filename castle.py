import pygame
import math
class Castle(pygame.sprite.Sprite):
	def __init__(self, xcoor, ycoor, filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename).convert()
		self.size = self.image.get_size()
		self.rect = self.image.get_rect()
		self.rect.x = xcoor
		self.rect.y = ycoor
		self.hp = 3
#		location = random.randrange(100,380)		#Chooses xcoordinate for castle's random location


	def getHit(self):
		self.hp -= 1		#if the castle gets hit, it loses 1 HP.  The game is won if the castle is struck 3 times
		if self.hp < 0:
			self.hp += 1
#		return hp
#		print("Hit!")

	def resetHP(self):
		self.hp = 3		#bug testing, in case we need to run it again

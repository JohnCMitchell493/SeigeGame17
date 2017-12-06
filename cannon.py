import pygame
import rock
import castle
import math
class Cannon(pygame.sprite.Sprite):
	def __init__(self, xcoor, ycoor, filename):
		pygame.sprite.Sprite.__init__(self)
		self.angle = 0		#angle and power/velocity default to 0
		self.power = 0
		self.image = pygame.image.load(filename).convert()
		self.size = self.image.get_size()
		self.image2 = pygame.transform.scale(self.image, (int(self.size[0]*.1), int(self.size[1]*.1)))
		self.rect = self.image2.get_rect()
		self.rect.x = xcoor
		self.rect.y = ycoor
	def angleChange(self, incdec):		#raises/lowers angle
		if incdec > 0:			#from controller, feed a positive or negative number, + for up
			if self.angle == 90:	#Angle should not exceed 90 degrees, if it tries to go higher it reverts to 90
				self.angle = 90
			else:			#Angle increases by 1
				self.angle += 1
		if incdec < 0:			#- for down
			if self.angle == 0:	#Angle should not be lower than 0 degrees, reverts to 0 if it tries to go lower
				self.angle = 0
			else:
				self.angle -= 1	#angle lowers by 1

	def powerChange(self, incdec):		#raises/lowers initial velocity
		if incdec > 0:			#from controller, feed a positive or negative number, + for up
			if self.power == 100:	#power should not exceed 100, if it tries to go higher it reverts to 100.  likely to change intesting
				self.power = 100
			else:			#power increases by 1
				self.power += 1
		if incdec < 0:			#- for down
			if self.power == 0:	#power should not be lower than 0, if it tries to go higher it reverts to 0.
				self.power = 0
			else:
				self.power -= 1	#power lowers by 1
	def shoot(self):
		return [self.angle,self.power]

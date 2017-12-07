import pygame
import cannon
import castle
import math

class Rock(pygame.sprite.Sprite):

	def __init__(self, xcoor, ycoor, filename):
		pygame.sprite.Sprite.__init__(self)
		self.x = 0
		self.y = 0
		self.image = pygame.image.load(filename).convert()
		self.size = self.image.get_size()
		self.image2 = pygame.transform.scale(self.image, (int(self.size[0]*1), int(self.size[1]*1)))
		self.rect = self.image2.get_rect()
		self.rect.x = xcoor
		self.rect.y = ycoor

	def calculateInitialVelocity(self,angle,velocity):
		self.angle = angle
		self.velocity = velocity
		self.time = 10000
		radangle = angle * (math.pi/180)
		compradangle = 180 - (angle + 90)
		radangle2 = compradangle * (math.pi/180)
		vely = (velocity * math.sin(radangle))/(math.sin(90))	#calculates initial x distance
		velx = (velocity * math.sin(radangle2))/(math.sin(90))	#calculates initial y distance
		return (velx, vely)

	def isOutside(self):
		if self.rect.x == 640 or self.rect.x >= 640:
			self.rect.x = 105
		elif self.rect.y == 480 or self.rect.y >= 480:
			self.rect.y = 420

	def iterCalcVelocity(self,xvel,yvel,time):
		xmove = xvel * time
		ymove = (yvel * time) - (.5*9.8*(time**2))
		return (xmove,ymove)

	def test(self,angle,velocity):
		results = self.calculateInitialVelocity(angle,velocity)
		velx = results[0]
		vely = results[1]
		self.rect.x += velx
		self.rect.y -= vely
		if self.isOutside() == True:
			self.rect.x = 105
			self.rect.y = 420
			print('Miss!')
			
	

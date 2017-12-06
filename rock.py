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
#		pygame.draw.circle(filename, (self.x,self.y), radius)

#	def checkCollision(self, object1, object2):
#		collision = pygame.sprite.collide_rect(object1, object2)
#		if collision == True:
#			return True
#		else:
#			return False

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
			return True
		elif self.rect.y == 480 or self.rect.y >= 480:
			return True
		else:
			return False

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
			
	def launch(self, angle, velocity):
		results = self.calculateInitialVelocity(angle,velocity)
		velx = results[0]
		vely = results[1]
		gravity = 9.8
		for i in range(1,self.time):
			results = self.iterCalcVelocity(velx,vely,i)
			xmove = results[0]
			ymove = results[1]
			self.rect.x = xmove + 105
			self.rect.y = 420-ymove
			print(self.rect.x)
			print(self.rect.y) 
#			self.rect.x = xmove+105
#			self.rect.y = -(ymove)+840
			pygame.time.wait(1000)
			if self.isOutside() == True:
				self.rect.x = 105
				self.rect.y = 420
				print('Miss!')
				break

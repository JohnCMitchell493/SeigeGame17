import pygame
import castle

class Rock(pygame.sprite.Sprite):

	def __init__(self, name, filename):
		self.name = name
		self.x = 0
		self.y = 0
		self.image = pygame.image.load("filename").convert()
		self.size = self.image.get_size()
		self.image2 = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
		self.rect = self.image2.get_rect()
#		pygame.draw.circle(filename, (self.x,self.y), radius)

	def checkCollision(self, sprite1, sprite2):
		collision = pygame.sprite.collide_rect(sprite1, sprite2)
		if collision == True:
			return True
		else:
			return False

	def launch(self, angle, velocity):
		self.angle = angle
		self.velocity = velocity
		gravity = 9.8		#gravity is constant
		self.time = 10000
		velx = (velocity * sin(angle))/(sin(90))	#calculates initial x distance
		vely = (velocity * sin(180-(angle+90)))/(sin(90))	#calculates initial y distance
#		xcoor = velx/i
#		ycoor = vely/i
		#ball.pygame.Rect.move(velx, vely)	#moves to coordinates calculated above.  This is also the initial velocity for the fromula loop below
		for i in range(self.time):		#formula loop.  i is time.  Does not actually loop every second, look into later
#			newvely = vely - (gravity*i)
			xmove = velx*i					#horizontal distance = speed*time, horizontal speed is constant because no wind
			ymove = 480-((vely)(i)-(.5)(gravity)((i)**2))		#vertical distance = (initial velocity)(time) - (1/2)(gravity)(time**2)
			self.rect.move(xmove,ymove)		#Move to new location based on calculated position
#			vely = newvely
			if checkCollision(self.rect, castle.rect) == False
				if xmove >= 400:				#if the rock's position moves to below the 'ground', or to beyond the 'right
					self.rect.move(500,500)		#border', the rock automatically relocates to a position outside the game
					return 'Miss!'
				if ymove >= 300:
					self.rect.move(500,500)
					return 'Miss!'

import random
from pygame import *

class Rock:
	def __init__(self, name, filename):
		self.name = name
		self.x = 0
		self.y = 0
		self.image = filename
		rocky = pygame.surface(5,5)		#creates rock rect
		ball = rocky.get_rect()			#creates rock rect surface
#		pygame.draw.circle(filename, (self.x,self.y), radius)

	def launch(self, angle, velocity):
		self.angle = angle
		self.velocity = velocity
		gravity = -9.8		#gravity is constant
		self.time = 1000
		velx = (velocity * sin(angle))/(sin(90))	#calculates initial x distance
		vely = (velocity * sin(180-(angle+90)))/(sin(90))	#calculates initial y distance
#		xcoor = velx/i
#		ycoor = vely/i
		ball.pygame.Rect.move(velx, vely)	#moves to coordinates calculated above.  This is also the initial velocity for the fromula loop below
		for i in range(1, self.time):		#formula loop.  i is time.  Does not actually loop every second, look into later
#			newvely = vely - (gravity*i)
			xmove = velx*i					#horizontal distance = speed*time, horizontal speed is constant because no wind
			ymove = (vely)(i)-(.5)(gravity)((i)**2)		#vertical distance = (initial velocity)(time) - (1/2)(gravity)(time**2)
			ball.pygame.Rect.move(xmove,ymove)		#Move to new location based on calculated position
#			vely = newvely

class castle:
	hp = 3
	def __init__(self, name, filename):
		self.name = name
		self.x = xcoor
		self.y = ycoor
		self.image = filename
		location = random.randrange(100,380)		#Chooses xcoordinate for castle's random location
		castle = pygame.rect(350,250,10,10)		#creates castle rect

	def getHit(self):
		hp -= 1		#if the castle gets hit, it loses 1 HP.  The game is won if the castle is struck 3 times
		return hp
		print("Hit!")

	def resetHP(self):
		hp = 3		#bug testing, in case we need to run it again

class cannon:
	def __init__(self, name, filename):
		self.name = name
		self.angle = 0		#angle and power/velocity default to 0
		self.power = 0
		self.image = filename
		my_font = pygame.font.SysFont("Times New Roman", 12)	#creates font pygame will use to display angle/velocity
		angle_label = my_font.render("Angle:" +str(self.angle), black)	#displays angle text
		power_label = my_font.render("Power:" +str(self.power), black)	#displays velocity text

	def angleChange(self, inc/dec):		#raises/lowers angle
		if inc/dec > 0:			#from controller, feed a positive or negative number, + for up
			if self.angle == 90:	#Angle should not exceed 90 degrees, if it tries to go higher it reverts to 90
				self.angle = 90
			else:			#Angle increases by 1
				self.angle += 1
		if inc/dec < 0:			#- for down
			if self.angle == 0:	#Angle should not be lower than 0 degrees, reverts to 0 if it tries to go lower
				self.angle = 0
			else:
				self.angle -= 1	#angle lowers by 1

	def powerChange(self, inc/dec):		#raises/lowers initial velocity
		if inc/dec > 0:			#from controller, feed a positive or negative number, + for up
			if self.power == 100:	#power should not exceed 100, if it tries to go higher it reverts to 100.  likely to change intesting
				self.power = 100
			else:			#power increases by 1
				self.power += 1
		if inc/dec < 0:			#- for down
			if self.power == 0:	#power should not be lower than 0, if it tries to go higher it reverts to 0.
				self.power = 0
			else:
				self.power -= 1	#power lowers by 1

	def shoot(self):
		Stone = rock()	#change when classes moved to their own files
		stone.launch(self.angle,self.power)	#shoots the damn boulder

class ground:
	def __init__(self, name, xcoor, ycoor, filename):
		self.name = name
		self.x = xcoor
		self.y = ycoor
		self.image = filename

#class Controller:
#	def __init__(self):
#		pygame.init()
#		self.display pygame.display.set_mode(400,300)
#		self.background = pygame.Surface(self.display.get_size())
#		self.rock
#		END = False
#		while !END:
#			for event in pygame.event.get():
#				if event.type == pygame.quit:
#					print("END")
#					END = True
#				elif event.type == pygame.KEYDOWN:
#					if event.key == pygame.K_UP:
#						
#					if event.key == pygame.K_DOWN:
#						
#					if event.key == pygame.K_LEFT:
#						
#					if event.key == pygame.K_RIGHT:
#						
#			self.display.blit(self.background)
#			self.sprites.draw(self.display)
















			

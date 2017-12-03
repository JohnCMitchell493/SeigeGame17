import pygame
class Rock:
	def __init__(self, name, filename):
		self.name = name
		self.image = pygame.image.load(filename)
		rocky = pygame.sprite.Sprite(self.image,20,20)		#creates rock rect
		ball = rocky.get_rect()			#creates rock rect surface
#		pygame.draw.circle(filename, (self.x,self.y), radius)

	def launch(self, angle, velocity):
		self.angle = angle
		self.velocity = velocity
		gravity = 9.8		#gravity is constant
		self.time = 1000
		velx = (velocity * sin(angle))/(sin(90))	#calculates initial x distance
		vely = (velocity * sin(180-(angle+90)))/(sin(90))	#calculates initial y distance
#		xcoor = velx/i
#		ycoor = vely/i
#		ball.pygame.Rect.move(velx, vely)	#moves to coordinates calculated above.  This is also the initial velocity for the fromula loop below
		for i in range(self.time):		#formula loop.  i is time.  Does not actually loop every second, look into later
#			newvely = vely - (gravity*i)
			xmove = velx*i					#horizontal distance = speed*time, horizontal speed is constant because no wind
			ymove = (vely)(i/10)-(.5)(gravity)((i/10)**2)		#vertical distance = (initial velocity)(time) - (1/2)(gravity)(time**2)
			ball.pygame.Rect.move(xmove,ymove)		#Move to new location based on calculated position
#			vely = newvely
#			if xmove >= 400:				#if the rock's position moves to below the 'ground', or to beyond the 'right 
#				ball.pygame.Rect.move(700,700)		#border', the rock automatically relocates to a position outside the game
#				return 'Miss!'
#			if ymove >= 300:
#				ball.pygame.Rect.move(700,700)
#				return 'Miss!'

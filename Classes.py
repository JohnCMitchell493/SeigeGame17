from pygame import *

class Rock:
	def __init__(self, name, radius, filename):
		self.name = name
		self.x = 0
		self.y = 0
		self.image = filename
		pygame.draw.circle(filename, (self.x,self.y), radius)

	def launch(self, angle, velocity, gravity):
		self.angle = angle
		self.velocity = velocity
		self.gravity = gravity
		self.time = 1000
		velx = (velocity * sin(angle))/(sin(90))
		vely = (velocity * sin(180-(angle+90)))/(sin(90))
		xcoor = velx/i
		ycoor = vely/i
		pygame.Rect.move(xcoor, ycoor)
		for i in range(1, 1000):
			ycoor~ = ycoor - (gravity*i)
			xmove = xcoor*i
			ymove = ycoor + ycoor~
			pygame.Rect.move(xcoor,ycoor~)
			ycoor = ycoor~


class castle:
	def __init__(self, name, xcoor, ycoor, filename):
		self.name = name
		self.x = xcoor
		self.y = ycoor
		self.image = filename

	hp = 9
	def getHit(self):
		hp -= 3
		return hp

class cannon:
	def __init__(self, name, , filename):
		self.name = name
		self.angle = angle
		self.image = filename

	def anim(self):

	def shoot(self):

class ground:
	def __init__(self, name, xcoor, ycoor, filename):
		self.name = name
		self.x = xcoor
		self.y = ycoor
		self.image = filename
		

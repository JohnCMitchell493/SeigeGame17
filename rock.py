import pygame
import cannon
import castle
import math

class Rock(pygame.sprite.Sprite):

	def __init__(self, xcoor, ycoor, filename):
		'''
		Description: Initializes the Rock class
		Parameters: self, xcoor, ycoor, filename - self is the default class parameter, xcoor and ycoor are the passed in coordinates, filename is the file's name
		Return: none
		'''
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
		'''
		Description: Caculates the initial velocity the rock launches at
		Parameters: self, angle, velocity - self is the default class parameter, angle is the rock's angle, velocity is the speed of the rock
		Return: velx, vely - velx is the velocity on the x axis, vely is the velocity on the y axis
		'''
		self.angle = angle
		self.velocity = velocity
		self.time = 10000
		radangle = angle * (math.pi/180)
		compradangle = 180 - (angle + 90)
		radangle2 = compradangle * (math.pi/180)
		vely = (velocity * math.sin(radangle))/(math.sin(90))	#calculates initial x distance
		velx = (velocity * math.sin(radangle2))/(math.sin(90))	#calculates initial y distance
		return (velx, vely)


	def iterCalcVelocity(self,xvel,yvel,time):
		'''
		Description: Calculates the velocity per iteration
		Parameters: self, xvel, yvel, time - self is the default class parameter, xvel and yvel is the x and y velocity, time is the time passed
		Return: xmove, ymove - xmove and ymove are the new values the rect will move to in coordinates
		'''
		xmove = xvel * time
		ymove = (yvel * time) - (.5*9.8*(time**2))
		return (xmove,ymove)

	

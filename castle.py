import pygame
import math
class Castle(pygame.sprite.Sprite):
	def __init__(self, xcoor, ycoor, filename):
		'''
		Description: Initializes the Castle class
		Parameters: self, xcoor, ycoor, filename - self is the default class parameter, xcoor and ycoor are the passed in coordinates, filename is the file's name
		Return: none
		'''
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename).convert()
		self.size = self.image.get_size()
		self.rect = self.image.get_rect()
		self.rect.x = xcoor
		self.rect.y = ycoor
		self.hp = 3


	def getHit(self): #Controls the castle's hp when hit
		'''
		Description: Lowers the castle's hp by one every time it gets hit
		Parameters: self - self is the default class parameter
		Return: none
		'''
		self.hp -= 1	#if the castle gets hit, it loses 1 HP.  
		if self.hp < 0: 	#prevents the hp from going lower than 0
			self.hp += 1

	def resetHP(self): #reset's castle's hp
		'''
		Description: Sets the castle's hp to 3
		Parameters: self - self is the default class paramter
		Return: none
		'''
		self.hp = 3		#sets the castle's hp back to 3

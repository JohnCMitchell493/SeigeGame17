import sys
import pygame
import cannon
import castle
import rock
import math
BLACK = (0, 0, 0)
class Controller:
	def __init__(self, width=640, height=480):
		'''
		Description: The main controller class that handles the images
		Parameters: self, width, height - self is the default class parameter, width is the screen width, height is the screen height
		Return:none
		'''
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.textfont = pygame.font.SysFont("helvetica", 15)
		self.titlefont = pygame.font.SysFont("helvetica", 90)
		self.startRect = pygame.Rect(180,320,80,30)
		self.quitRect = pygame.Rect(380,320,80,30)
		self.cannon = cannon.Cannon(0, 420, "cannon.jpg")
		self.castle = castle.Castle(450, 310, "castle.png")
		self.rock = rock.Rock(105,420, "rocky.jpg")
		self.castlerect = self.castle.rect
		self.cannonSprite = pygame.sprite.Group(self.cannon) ##Used for drawing the cannon sprite
		self.castleSprite = pygame.sprite.Group(self.castle) ##Used for drawing the castle sprite
		self.rockSprite = pygame.sprite.Group(self.rock) ##Used for drawing the rock sprite
		self.shot = 0
		self.angle = 0
		self.velocity = 0
		self.ixvelocity =0
		self.iyvelocity = 0
		self.rocktime = 0
		self.bullets = 5
	#Start Button
	def startButton(self):
		'''
		Description: Draws the Start button
		Parameters: self - self is the default class parameter
		Return: none
		'''
		start = pygame.draw.rect(self.screen, (192,192,192), self.startRect, 0)#Draws start the rectangle
		startGame = self.textfont.render("Start", 1, (BLACK))
		self.screen.blit(startGame, (205, 325))	#Blits the text/button to the rect
	#Retry Button
	def retryButton(self):
		'''
		Description: Draws the Retry button
		Parameters:	self - self is the default class parameter
		Return: none
		'''
		start = pygame.draw.rect(self.screen, (192,192,192), self.startRect, 0)#Draws start the rectangle
		startGame = self.textfont.render("Retry", 1, (BLACK))
		self.screen.blit(startGame, (205, 325))	#Blits the text/button to the rect

	#Quit Button
	def quitButton(self):
		'''
		Description: Draws the Quit button
		Parameters: self - self is the default class parameter
		Return: none
		'''
		quit = pygame.draw.rect(self.screen, (192,192,192), self.quitRect, 0)#Draws quit the rectangle
		quitGame = self.textfont.render("Quit", 1, (BLACK))
		self.screen.blit(quitGame, (410, 325))	#Blits the text/button to the rect

	#Main title text
	def titleText(self):
		'''
		Description: Draws the Title text
		Parameters: self - self is the default class parameter
		Return: none
		'''
		tText = self.titlefont.render("SIEGE", 1, (174,34,34))
		self.screen.blit(tText, (208,100))

	def victoryText(self):
		'''
		Description: Draws the Victory text
		Parameters: self - self is the default class parameter
		Return: none
		'''
		vText = self.titlefont.render("VICTORY", 1, (174,34,34))
		self.screen.blit(vText, (160,100))

	def defeatText(self):
		'''
		Description: Draws the Defeat text
		Parameters: self - self is the default class parameter
		Return: none
		'''
		dText = self.titlefont.render("DEFEAT", 1, (174,34,34))
		self.screen.blit(dText, (180,100))
		
	def rockUpdate(self):
		'''
		Description: Updates the rock's position
		Parameters: self - self is the default class parameter
		Return: none
		'''
		if self.shot == 1: #controls rock movement
			if self.rocktime == 0:
				startup = self.rock.calculateInitialVelocity(self.angle,self.velocity)
				self.ixvelocity = startup[0]
				self.iyvelocity = startup[1]
				move = self.rock.iterCalcVelocity(self.ixvelocity,self.iyvelocity,self.rocktime)
				self.rock.rect.x = 105 + move[0]
				self.rock.rect.y = 420 - move[1]
				self.rocktime += 1
			else:
				move = self.rock.iterCalcVelocity(self.ixvelocity,self.iyvelocity,self.rocktime)
				self.rock.rect.x = 105 + move[0]
				self.rock.rect.y = 420 - move[1]
				self.rocktime += 1

	def mainLoop(self):
		'''
		Description: mainLoop is the main event processing loop that takes data from all other parts of the project
		Parameters: self - self is the default class parameter
		Return: none
		'''
		#Event Processing
		done = False #when set to true and followed by pygame.quit() and sys.exit(), closes pygame and its window
		start = False #When it is false, 'start' will allow the game to be quit by clicking the quit button
		title = True #when set to false, pressing S will not start the game over again
		retry = False #When set to true and 'title' == False, switches screen to victory/defeat screen
		titleScreen = pygame.image.load("background.jpg")
		pygame.key.set_repeat(1,50) #allows directions to be held for easier angle/velocity number management
		while not done:
			self.startButton()#display title screen with start and quit options
			self.quitButton()
			self.titleText()
			if title == False:
				retry = False
				self.screen.fill((0,225,225))
				self.rockSprite.draw(self.screen)
				self.cannonSprite.draw(self.screen)
				self.castleSprite.draw(self.screen)
				my_font = pygame.font.SysFont("Times New Roman", 12)	#creates font pygame will use to display angle/velocity
				angle_label = my_font.render("Angle:" +str(self.cannon.angle), 1, BLACK)	#displays angle text
				power_label = my_font.render("Power:" +str(self.cannon.power), 1, BLACK)	#displays velocity text
				bullet_label = my_font.render("Shots:" +str(self.bullets),1, BLACK)
				self.screen.blit(angle_label, (0,0))
				self.screen.blit(power_label, (50,0))
				self.screen.blit(bullet_label, (100,0))
				if self.castle.hp == 0 or self.bullets == 0:
					self.screen.fill(BLACK)
					retry = True
					if self.castle.hp == 0: #The game is won if the castle is struck 3 times
						self.victoryText()
						if self.bullets <1:
							self.bullets+=1 #prevents victory screen from merging with defeat screen
					if self.bullets == 0:
						self.defeatText()
					self.quitButton()
					self.retryButton()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						angle = 1
						self.cannon.angleChange(angle)
					if event.key == pygame.K_DOWN:
						angle = -1
						self.cannon.angleChange(angle)
					if event.key == pygame.K_LEFT:
						power = -1
						self.cannon.powerChange(power)
					if event.key == pygame.K_RIGHT:
						power = 1
						self.cannon.powerChange(power)
					if event.key == pygame.K_SPACE:
						self.shot = 1
						results = self.cannon.shoot()
						self.angle = results[0]
						self.velocity = results[1]
						if self.bullets > 0:
							self.bullets -=1
				if event.type == pygame.MOUSEBUTTONDOWN: #allows for mouse collision with buttons
					mpos = pygame.mouse.get_pos()
					if self.startRect.collidepoint(mpos):
							self.bullets = 5
							self.angle = 0
							self.velocity = 0
							start = True
							title = False
							self.castle.resetHP()
							self.rock.rect.x = 105
							self.rock.rect.y = 420
					if self.quitRect.collidepoint(mpos):
						if start == False or retry == True:
							done = True
							pygame.quit()
							sys.exit()

			try:
				if self.shot == 1: #controls the outofbounds state of the game and whether or not rock hit the castle
					if (pygame.sprite.collide_rect(self.castle, self.rock)):
						self.castle.getHit()
						self.rock.rect.x = 105
						self.rock.rect.y = 420
						self.rocktime = 0
						self.shot = 0
						if self.castle.hp != 0:
							self.screen.fill((255, 0, 0))
					if self.rock.rect.x == 640 or self.rock.rect.x >= 640:
						self.rock.rect.x = 105
						self.rock.rect.y = 420
						self.rocktime = 0
						self.shot = 0


						
					if self.rock.rect.y == 480 or self.rock.rect.y >= 480:
						self.rock.rect.x = 105
						self.rock.rect.y = 420
						self.rocktime = 0
						self.shot = 0

			finally:
				self.rockUpdate() 
				pygame.display.flip() #updates the current screen
				self.screen.blit(self.background, (0,0))
				self.screen.blit(titleScreen,(0,0))


def main():
	main_window = Controller()
	main_window.mainLoop()
main()

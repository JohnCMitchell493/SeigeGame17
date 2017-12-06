import sys
import pygame
import cannon
import castle
import rock
import math
BLACK = (0, 0, 0)
class Controller:
	def __init__(self, width=640, height=480):
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
		#self.rockSprite = []
	#Start Button
	def startButton(self):
		start = pygame.draw.rect(self.screen, (192,192,192), self.startRect, 0)#Draws start the rectangle
		startGame = self.textfont.render("Start", 1, (BLACK))
		self.screen.blit(startGame, (205, 325))	#Blits the text/button to the rect
	#Retry Button
	def retryButton(self):
		start = pygame.draw.rect(self.screen, (192,192,192), self.startRect, 0)#Draws start the rectangle
		startGame = self.textfont.render("Retry", 1, (BLACK))
		self.screen.blit(startGame, (205, 325))	#Blits the text/button to the rect

	#Quit Button
	def quitButton(self):
		quit = pygame.draw.rect(self.screen, (192,192,192), self.quitRect, 0)#Draws quit the rectangle
		quitGame = self.textfont.render("Quit", 1, (BLACK))
		self.screen.blit(quitGame, (410, 325))	#Blits the text/button to the rect

	#Main title text
	def titleText(self):
		tText = self.titlefont.render("SIEGE", 1, (174,34,34))
		self.screen.blit(tText, (208,100))

	def mainLoop(self):
		#Event Processing
		done = False
		start = False #If false, causes while 'while not done' to become 'True' and closes the game window
		title = True #If false, pressing S will not start the game over again
		retry = False
		titleScreen = pygame.image.load("background.jpg")
		pygame.key.set_repeat(1,50)
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
				self.screen.blit(angle_label, (0,0))
				self.screen.blit(power_label, (50,0))
				if self.castle.hp == 0:
					self.screen.fill(BLACK)
					retry = True
					"import victory background for x amount of seconds"
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
						ang = results[0]
						vel = results[1]
						self.rock.launch(ang,vel)
					if event.key == pygame.K_q:
						if start == False or retry == True:
							done = True
							pygame.quit()
							sys.exit()
					if event.key == pygame.K_s:
						if retry != True:
							start = True #start == FALSE: will set this to true when game starts to prevent reloading the game
							title = False
							self.castle.resetHP()
							self.rock.rect.x = 105
							self.rock.rect.y = 420
					if event.key == pygame.K_r:
						if retry == True:
							start = True #start == FALSE: will set this to true when game starts to prevent reloading the game
							title = False
							self.castle.resetHP()
							self.rock.rect.x = 105
							self.rock.rect.y = 420
				if event.type == pygame.MOUSEBUTTONDOWN:
					mpos = pygame.mouse.get_pos()
					if self.startRect.collidepoint(mpos):
						if retry == True:
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
						#self.mainGame()
#					if event.key == pygame.MOUSEBUTTONDOWN:
#						mouse = pygame.mouse.get_pos()
#						print(mouse)
#						if quit.collide(mouse):
#							stuff that would happen when
#							the mouse hits the start button
			try:
				if self.shot == 1:
					if (pygame.sprite.collide_rect(self.castle, self.rock)):
						self.castle.getHit()
						self.rock.rect.x = 105
						self.rock.rect.y = 420
						self.shot = 0
						self.screen.fill((255, 0, 0))
			finally:
				pygame.display.flip()
				self.screen.blit(self.background, (0,0))
				self.screen.blit(titleScreen,(0,0))


def main():
	main_window = Controller()
	main_window.mainLoop()
main()


import sys
import pygame
import cannon
import castle
import rock
import cmath

class Controller:
	def __init__(self, width=640, height=480):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.cannon = cannon
		self.castle = castle
		self.rock = rock
		self.textfont = pygame.font.SysFont("helvetica", 15)
		self.startRect = pygame.Rect(180,320,80,30)
		self.quitRect = pygame.Rect(380,320,80,30)
		self.cannon = cannon.Cannon("Cannon","cannon.jpg")
		self.castle = castle.Castle("Castle","castle.png")
		#self.sprites = pygame.sprite.Group((self.cannon)) #Used for drawing the sprites, still a work in progress 
	#Start Button
	def startButton(self):
		start = pygame.draw.rect(self.screen, (192,192,192), self.startRect, 0)#Draws start the rectangle
		startGame = self.textfont.render("Start", 1, (255, 255, 0))
		self.screen.blit(startGame, (205, 325))	#Blits the text/button to the rect



	#Quit Button
	def quitButton(self):
		quit = pygame.draw.rect(self.screen, (192,192,192), self.quitRect, 0)#Draws quit the rectangle
		quitGame = self.textfont.render("Quit", 1, (255, 255, 0))
		self.screen.blit(quitGame, (410, 325))	#Blits the text/button to the rect


		
	#def mainGame(self): #Main Game screen
		
#		self.screen.blit(cannon.Cannon("Cannon", "cannon.jpg"),(0,0)) #Might not be necessary
#		self.screen.blit(self.cannon(angle_label, (200,200))) 
#		self.sprites.draw(self.screen) draws the sprites the the screen(work in progress)


	def mainLoop(self):


		#Event Processing
		done = False
		start = False
		title = False
		while not done:
			titleScreen = pygame.image.load("background.jpg")
			self.startButton()#display title screen with start and quit options
			self.quitButton()
			if title == True:
				self.screen.fill((0,225,225))
#			if "insert castle syntax here" hp == 0:
#				title = False #stops the screen from being blitted blue
#				start = False #Allows 'q' to quit again
#				"import victory background for x amount of seconds"
#				put retry screen
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
						self.cannon.shoot()
					if event.key == pygame.K_s or pygame.K_r:
						start = True #start == FALSE: will set this to true when game starts to prevent reloading the game
						title = True
						#self.mainGame()
					if event.key == pygame.K_q: 
						if start == False:
						    done = True
						    pygame.quit()
						    sys.exit()
#					if event.key == pygame.MOUSEBUTTONDOWN:
#						mouse = pygame.mouse.get_pos()
#						print(mouse)
#						if quit.collide(mouse):
#							stuff that would happen when 
#							the mouse hits the start button
			pygame.display.update()
			self.screen.blit(self.background, (0,0))
			self.screen.blit(titleScreen,(0,0))
			

 




def main():
	main_window = Controller()
	main_window.mainLoop()
main()

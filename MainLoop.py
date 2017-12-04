import sys
import pygame
import cannon
import castle
import rock
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
		
	#Start Button
	def startButton(self):
		pygame.draw.rect(self.screen, (192,192,192), self.startRect, 0)
		#Draws the rectangle
		startGame = self.textfont.render("Start", 1, (255, 255, 0))
		self.screen.blit(startGame, (150, 200))	
		#Blits the text/button to the rect
		pygame.display.update()
		#Updates the screen
		
	#Quit Button
	def quitButton(self):
		quit = pygame.draw.rect(self.screen, (192,192,192), self.quitRect, 0)
		#Draws the rectangle
		quitGame = self.textfont.render("Quit", 1, (255, 255, 0))
		self.screen.blit(quitGame, (250, 200))	
		#Blits the text/button to the rect
		pygame.display.update()
		#Updates the screen
		
	def mainGame(self):
		#Main Game screen
		self.screen.fill((0,225,225))
		
		
		
		
	def mainLoop(self):
		self.screen.fill((0,225,225))
		pygame.display.update()
		self.startButton()
		self.quitButton()
		#display title screen with start and quit options

		self.cannon = cannon.Cannon("Cannon","cannon.jpg")
		self.castle = castle.Castle("Castle","castle.png")
		self.rock = rock.Rock("Rocky","rocky.png")
		
		#Event Processing
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						angle = 1
						cannon.angleChange(angle)
					if event.key == pygame.K_DOWN:
						angle = -1
						cannon.angleChange(angle)
					if event.key == pygame.K_LEFT:
						power = -1
						cannon.powerChange(power)
					if event.key == pygame.K_RIGHT:
						power = 1
						cannon.powerChange(power)
					if event.key == pygame.K_SPACE:
						cannon.shoot()
					if event.key == pygame.K_q:
					    #if start == FALSE: will set this to true when game starts to prevent 
						done = True
						pygame.quit()
						sys.exit()
					#if event.key == pygame.S_s:
					#if start.collide(mouse):
						#stuff that would happen when 
						#the mouse hits the start button
			pygame.display.update()






			#Victory Screen 


			#Post Victory screen with quit and retry options

def main():
	main_window = Controller()
	main_window.mainLoop()
main()

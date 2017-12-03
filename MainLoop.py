import pygame
import cannon
import castle
import rock

class Controller:
	def __init__(self, width=400, height=300):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode(width,height)
		self.background = pygame.Surface(self.screen.get_size())
		self.cannon = cannon
		self.castle = castle
		self.rock = rock
		self.textfont = pygame.font.SysFont("helvetica", 15)
		self.startRect = pygame.Rect(150,200,40,20)
		self.quitRect = pygame.Rect(250,200,40,20)
		
	#Start Button
	def startButton(self):
		start = pygame.draw.rect(self.screen, (192,192,192), self.startRect, width=0)
		#Draws the rectangle
		startGame = self.textfont.render("Start", 1, (255, 255, 0))
		self.screen.blit(start, (150, 200))
		self.screen.blit(startGame, (150, 200))	
		#Blits the text/button to the rect
		pygame.display.update()
		#Updates the screen
		
	#Quit Button
	def quitButton(self):
		quit = pygame.draw.rect(self.screen, (192,192,192), self.quitRect, width=0)
		#Draws the rectangle
		quitGame = self.textfont.render("Quit", 1, (255, 255, 0))
		self.screen.blit(quit, (250, 200))
		self.screen.blit(quitGame, (250, 200))	
		#Blits the text/button to the rect
		pygame.display.update()
		#Updates the screen
		
		
	def mainGame(self):
		#Main Game screen
		self.background.fill((0,225,225))
		
		
		
		
	def mainLoop(self):
		self.background.fill((0,225,225))
		self.startButton()
		self.quitButton()
		#display title screen with start and quit options

		self.cannon = cannon.cannon("Cannon")# add the filename,xcoor,ycoor
		self.castle = castle.castle("Castle")# add the filename,xcoor,ycoor
		self.rock = rock.Rock("Rocky")# add the filename,xcoor,ycoor
		
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
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse = pygame.mouse.get_pos()
					if quit.collide(mouse):
						done = True
						pygame.quit()
						sys.exit()
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

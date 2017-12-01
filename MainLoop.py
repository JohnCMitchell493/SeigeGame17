import pygame
import cannon
import castle
import rock

class Controller:
	def __init__(self, width=400, height=300):
		pygame.init()
		self.width = width
		self.height = height
		self.display = pygame.display.set_mode(width,height)
		self.background = pygame.Surface(self.display.get_size())
		self.cannon = cannon
		self.castle = castle
		self.rock = rock
	def mainLoop(self):
		while True:
			#display title screen with start and quit options
			self.background.fill((0,225,225))
			mouse = pygame.mouse.get_pos()
			
			#Start Button
			textfont = pygame.font.SysFont("helvetica", 15)
			startGame = textfont.render("Start", 1, (255, 255, 0))
			screen.blit(startGame, (100, 300))
			
			#Quit Button
			textfont = pygame.font.SysFont("helvetica", 15)
			quitGame = textfont.render("Quit", 1, (255, 255, 0))
			screen.blit(quitGame, (300, 300))
			
			self.cannon = cannon.Cannon("Cannon")
			
			#Event Processing
			done = False
			while not done:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						done = True
					elif event.type == pygame.KEYDOWN:
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
					elif event.type == pygame.MOUSEBUTTONDOWN:
						mouse_pos = pygame.mouse.get_pos()
				self.display.blit(self.background)
				self.sprites.draw(self.display)
		
		
		
				#Main Game screen 
		
		
		
				#Victory Screen 


				#Post Victory screen with quit and retry options
		
def main():
	main_window = Controller()
	main_window.mainLoop()
main()

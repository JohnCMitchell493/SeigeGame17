import pygame
import cannon
import castle
import rock

class Controller:
	def __init__(self, width=400, height=300)
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
			textfont = pygame.font.SysFont("helvetica", 15)
			start = textfont.render("Start" 1, (255, 255, 0))
			screen.blit(label, (100, 300))
			self.background.fill((0,225,225))
			textfont = pygame.font.SysFont("helvetica", 15)
			start = textfont.render("Start" 1, (255, 255, 0))
			screen.blit(label, (300, 300))
			self.cannon = cannon.Cannon("Rock")
			done = False
			while not done:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						done = True
					elif event.type = pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							self.hero.move_up()
						if event.key == pygame.K_DOWN:
							self.hero.move_up()
						if event.key == pygame.K_LEFT:
							self.hero.move_up()
						if event.key == pygame.K_RIGHT:
							self.hero.move_up()
				self.display.blit(self.background)
				self.sprites.draw(self.display)
		
		
		
				#Main Game screen 
		
		
		
				#Victory Screen 


				#Post Victory screen with quit and retry options
		
def main():
	main_window = Controller()
	main_window.mainLoop()
main()

import pygame

class PYGAME_WINDOW:
	
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((300,100))

	def Prepare(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True
	def Reveal(self):
		pass

import pygame

from constants import CONSTANTS

myConstants = CONSTANTS()

class PYGAME_WINDOW:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((myConstants.pygameWindowWidth, myConstants.pygameWindowDepth))

	def Prepare(self):
		self.screen.fill((255,255,255))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True

	def Reveal(self):
		pygame.display.update()

	def Draw_Black_Circle(self,x,y):
		revY = myConstants.pygameWindowDepth - y
		pygame.draw.circle(self.screen,(0,0,0),(x,revY),10)

	def Draw_Black_Line(self, xtip, ytip, xbase, ybase, width):
		pygame.draw.line(self.screen,(0,0,0),(xtip,ytip),(xbase,ybase),width)

import pygame

from threading import Timer

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


	def drawImage(self):
		hand = pygame.image.load('hand.png')
		hand = pygame.transform.scale(hand, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(hand, (myConstants.pygameWindowDepth/2, 0))
	def moveLeft(self):
		left = pygame.image.load('pointLeft.png')
		left = pygame.transform.scale(left, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(left, (myConstants.pygameWindowDepth/2, 0))
	def moveRight(self):
		right = pygame.image.load('point.jpeg')
		right = pygame.transform.scale(right, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(right, (myConstants.pygameWindowDepth/2, 0))
	def moveUp(self):
		up = pygame.image.load('point.jpeg')
		up = pygame.transform.rotate(up, 90)
		up = pygame.transform.scale(up, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(up, (myConstants.pygameWindowDepth/2, 0))
	def moveDown(self):
		down = pygame.image.load('point.jpeg')
		down = pygame.transform.rotate(down, 270)
		down = pygame.transform.scale(down, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(down, (myConstants.pygameWindowDepth/2, 0))
	def success(self):
		success = pygame.image.load('thumb.jpeg')
		success = pygame.transform.scale(success, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(success, (myConstants.pygameWindowDepth/2, 0))
	def fail(self):
		fail = pygame.image.load('thumb.jpeg')
		fail = pygame.transform.rotate(fail, 180)
		fail = pygame.transform.scale(fail, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(fail, (myConstants.pygameWindowDepth/2, 0))



	def num0(self):
		num0 = pygame.image.load('number0.png')
		num0 = pygame.transform.scale(num0, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num0, (myConstants.pygameWindowDepth/2, 0))
	def num1(self):
		num1 = pygame.image.load('number01.jpg')
		num1 = pygame.transform.scale(num1, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num1, (myConstants.pygameWindowDepth/2, 0))
	def num2(self):
		num2 = pygame.image.load('number02.jpg')
		num2 = pygame.transform.scale(num2, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num2, (myConstants.pygameWindowDepth/2, 0))
	def num3(self):
		num3 = pygame.image.load('number03.jpg')
		num3 = pygame.transform.scale(num3, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num3, (myConstants.pygameWindowDepth/2, 0))
	def num4(self):
		num4 = pygame.image.load('number04.jpg')
		num4 = pygame.transform.scale(num4, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num4, (myConstants.pygameWindowDepth/2, 0))
	def num5(self):
		num5 = pygame.image.load('number05.jpg')
		num5 = pygame.transform.scale(num5, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num5, (myConstants.pygameWindowDepth/2, 0))
	def num6(self):
		num6 = pygame.image.load('number06.jpg')
		num6 = pygame.transform.scale(num6, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num6, (myConstants.pygameWindowDepth/2, 0))
	def num7(self):
		num7 = pygame.image.load('number07.jpg')
		num7 = pygame.transform.scale(num7, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num7, (myConstants.pygameWindowDepth/2, 0))
	def num8(self):
		num8 = pygame.image.load('number08.jpg')
		num8 = pygame.transform.scale(num8, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num8, (myConstants.pygameWindowDepth/2, 0))
	def num9(self):
		num9 = pygame.image.load('number09.jpg')
		num9 = pygame.transform.scale(num9, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(num9, (myConstants.pygameWindowDepth/2, 0))

	def showSign(self, num):
		if num == 0:
			self.num0()
		elif num == 1:
			self.num1()
		elif num == 2:
			self.num2()
		elif num == 3:
			self.num3()
		elif num == 4:
			self.num4()
		elif num == 5:
			self.num5()
		elif num == 6:
			self.num6()
		elif num == 7:
			self.num7()
		elif num == 8:
			self.num8()
		elif num == 9:
			self.num9()

	def dig0(self):
		dig0 = pygame.image.load('zero.png')
		dig0 = pygame.transform.scale(dig0, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig0, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig1(self):
		dig1 = pygame.image.load('one.png')
		dig1 = pygame.transform.scale(dig1, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig1, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig2(self):
		dig2 = pygame.image.load('two.png')
		dig2 = pygame.transform.scale(dig2, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig2, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig3(self):
		dig3 = pygame.image.load('three.png')
		dig3 = pygame.transform.scale(dig3, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig3, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig4(self):
		dig4 = pygame.image.load('four.png')
		dig4 = pygame.transform.scale(dig4, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig4, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig5(self):
		dig5 = pygame.image.load('five.png')
		dig5 = pygame.transform.scale(dig5, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig5, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig6(self):
		dig6 = pygame.image.load('six.png')
		dig6 = pygame.transform.scale(dig6, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig6, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig7(self):
		dig7 = pygame.image.load('seven.png')
		dig7 = pygame.transform.scale(dig7, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig7, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig8(self):
		dig8 = pygame.image.load('eight.png')
		dig8 = pygame.transform.scale(dig8, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig8, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
	def dig9(self):
		dig9 = pygame.image.load('nine.png')
		dig9 = pygame.transform.scale(dig9, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(dig9, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))

	def hideDigit(self):
		blank = pygame.image.load('blank.png')
		blank= pygame.transform.scale(blank, (myConstants.pygameWindowDepth/2, myConstants.pygameWindowDepth/2))
		self.screen.blit(blank, (myConstants.pygameWindowDepth/2,myConstants.pygameWindowDepth/2))
		print("HIDDEN")

	def showNum(self, num):
		if num == 0:
			self.dig0()
		elif num == 1:
			self.dig1()
		elif num == 2:
			self.dig2()
		elif num == 3:
			self.dig3()
		elif num == 4:
			self.dig4()
		elif num == 5:
			self.dig5()
		elif num == 6:
			self.dig6()
		elif num == 7:
			self.dig7()
		elif num == 8:
			self.dig8()
		elif num == 9:
			self.dig9()
		#t = Timer(2.0, self.hideDigit,args=())
		#t.start()

	def numAttempt(self, database, userName, randNumber):
		userRecord = database[userName][1]
		index = 'digit' + str(randNumber) + 'attempted'
		numTimes = userRecord[index]
		string = 'Attempt Number: ' + str(numTimes + 1)

		font = pygame.font.SysFont("comicsansms", 20)
		text = font.render(string , True, (0, 128, 0))
		self.screen.blit(text,(myConstants.pygameWindowDepth / 8,myConstants.pygameWindowDepth / 2))

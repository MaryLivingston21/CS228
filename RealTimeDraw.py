from pygameWindow import PYGAME_WINDOW
from constants import CONSTANTS

import random

pygameWindow = PYGAME_WINDOW()
myConstants = CONSTANTS()

x = 300
y = 300

def Perturb_Circle_Position():
	global x, y
	fourSideDieRoll = random.randint(1,4)
	if fourSideDieRoll == 1:
		x -= 1
	elif fourSideDieRoll == 2:
		x += 1
	elif fourSideDieRoll == 3:
		y -= 1
	elif fourSideDieRoll == 4:
		y += 1

#print pygameWindow

while True:
	pygameWindow.Prepare()
	pygameWindow.Draw_Black_Circle(x,y)
	Perturb_Circle_Position()
	pygameWindow.Reveal()

import sys
sys.path.insert(0,'..')
from Leap import *


from pygameWindow import PYGAME_WINDOW
from constants import CONSTANTS

import random

pygameWindow = PYGAME_WINDOW()
myConstants = CONSTANTS()

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

#def Perturb_Circle_Position():
	#global x, y
	#fourSideDieRoll = random.randint(1,4)
	#if fourSideDieRoll == 1:
		#x -= 1
	#elif fourSideDieRoll == 2:
		#x += 1
	#elif fourSideDieRoll == 3:
		#y -= 1
	#elif fourSideDieRoll == 4:
		##y += 1

controller = Controller()

#print pygameWindow

def Handle_Frame(frame, xMin, xMax, yMin, yMax):
	global x, y
	hand = frame.hands[0]
	fingers = hand.fingers
	indexFingerList = fingers.finger_type(Finger.TYPE_INDEX)
	indexFinger = indexFingerList[0]

	distalPhalanx = indexFinger.bone(Bone.TYPE_DISTAL)
	tip = distalPhalanx.next_joint

	x = tip[0]
	y = tip[1]

	#print(tip)

	if (x < xMin):
		xMin = x
	if (x > xMax):
		xMax = x
	if (y < yMin):
		yMin = y
	if y > yMax:
		yMax = y

	#print xMin, xMax, yMin, yMax

def Scale(n,oMin,oMax,newMin,newMax):
	newN = 0
	if(oMin == oMax):
		newN = n
		return n
	old = oMax - oMin
	new = newMax - newMin
	newN = (n * new) / old
	newN = n + newMin
	return n

while True:
	pygameWindow.Prepare()
	frame = controller.frame()
	if len(frame.hands) != 0:
		#print "hand detected"
		Handle_Frame(frame, xMin, xMax, yMin, yMax)
		pyGameX = Scale(x, xMin, xMax, 0, myConstants.pygameWindowWidth)
		pyGamey = Scale(y, yMin, yMax, 0, myConstants.pygameWindowDepth)
		pygameWindow.Draw_Black_Circle(int(pyGameX),int(pyGamey))
		#print pyGameX, pyGamey
	#Perturb_Circle_Position()
	pygameWindow.Reveal()

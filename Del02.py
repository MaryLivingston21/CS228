import random
import sys
sys.path.insert(0,'..')
from Leap import *


from pygameWindow import PYGAME_WINDOW
from constants import CONSTANTS

pygameWindow = PYGAME_WINDOW()
myConstants = CONSTANTS()
controller = Controller()

#center position
x = int(myConstants.pygameWindowWidth / 2)
y = int(myConstants.pygameWindowDepth / 2)

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

def Handle_Frame(frame):

	hand = frame.hands[0]
	fingers = hand.fingers

	for finger in fingers:
		Handle_Finger(finger)


def Scale(n, oMin, oMax, newMin, newMax):
	if(oMin == oMax):
		newN = n
		return newN
	old = oMax - oMin
	new = newMax - newMin
	newN = (n * new) / old
	newN = newN + newMin
	return newN


def Handle_Finger(finger):
	for b in range(0,4):
		bone = finger.bone(b)
		Handle_Bone(bone, 1)


def Handle_Bone(bone, width):
	base = bone.prev_joint
	tip = bone.next_joint

	pygameWindow.Draw_Black_Line(Handle_Vector_FromLeap(tip), Handle_Vector_FromLeap(base), width)
	#print tip, base


def Handle_Vector_FromLeap(v):
	global x, y
	global xMin, xMax, yMin, yMax
	x = Scale(v[0], xMin, xMax, 0, myConstants.pygameWindowWidth)
	y = Scale(v[2], xMin, xMax, 0, myConstants.pygameWindowDepth) #fix this
	#print(x,y)

	if (x < xMin):
		xMin = x
	if (x > xMax):
		xMax = x
	if (y < yMin):
		yMin = y
	if y > yMax:
		yMax = y

	return x, y


while True:
	pygameWindow.Prepare()
	frame = controller.frame()
	if len(frame.hands) != 0:
		Handle_Frame(frame)
	pygameWindow.Reveal()

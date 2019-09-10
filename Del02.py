import random
import sys
sys.path.insert(0,'..')
from Leap import *


from pygameWindow import PYGAME_WINDOW
from constants import CONSTANTS

pygameWindow = PYGAME_WINDOW()
myConstants = CONSTANTS()
controller = Controller()

x = int(constants.pygameWindowWidth / 2)
y = int(constants.pygameWindowDepth / 2)
xMin = 500.0
xMax = -500.0
yMin = 500.0
yMax = -500.0

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

def Handle_Frame(frame, xMin, xMax, yMin, yMax):

	hand = frame.hands[0]
	fingers = hand.fingers

	for finger in fingers:
		Handle_Finger(finger)
	#print finger
	exit()
	# indexFingerList = fingers.finger_type(Finger.TYPE_INDEX)
	# indexFinger = indexFingerList[0]
	#
	# distalPhalanx = indexFinger.bone(Bone.TYPE_DISTAL)
	# tip = distalPhalanx.next_joint
	#
	# x = tip[0]
	# y = tip[1]
	#
	# #print(tip)
	#
	# if (x < xMin):
	# 	xMin = x
	# if (x > xMax):
	# 	xMax = x
	# if (y < yMin):
	# 	yMin = y
	# if y > yMax:
	# 	yMax = y

	#print xMin, xMax, yMin, yMax

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

		Handle_Bone(bone, 4 - b)

def Handle_Bone(bone, width):
	base = bone.prev_joint
	tip = bone.next_joint
	print base, tip

def Handle_Vector_FromLeap(v):
	global x, y
	global xMin, xMax, yMin, yMax
	x = Scale(v[0]), xMin, xMax, 0, myConstants.pygameWindowWidth)
	y = Scale(v[2]), xMin, xMax, 0, myConstants.pygameWindowDepth)
	print(x,y)

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
		#print "hand detected"
		Handle_Frame(frame, xMin, xMax, yMin, yMax)
		#pyGameX = Scale(x, xMin, xMax, 0, myConstants.pygameWindowWidth)
		#pyGamey = Scale(y, yMin, yMax, 0, myConstants.pygameWindowDepth)
		#pygameWindow.Draw_Black_Circle(int(pyGameX),int(pyGamey))
		#print pyGameX, pyGamey
	#Perturb_Circle_Position()
	pygameWindow.Reveal()

import sys
sys.path.insert(0,'../..')
from Leap import *

import numpy as np
import random
import pickle


from pygameWindow import PYGAME_WINDOW
from constants import CONSTANTS

pygameWindow = PYGAME_WINDOW()
myConstants = CONSTANTS()
controller = Controller()

# load in classifier
clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros((1,30),dtype='f')

#center position
x = int(myConstants.pygameWindowWidth / 2)
y = int(myConstants.pygameWindowDepth / 2)

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0



def Handle_Frame(frame):
	global x, y, xMin, xMax, yMin, yMax
	hand = frame.hands[0]
	fingers = hand.fingers
	for finger in fingers:
		Handle_Finger(finger)


def Scale(n, oMin, oMax, newMin, newMax):
	n = n - oMin
	if(oMin == oMax):
		return n
	old = oMax - oMin
	new = newMax - newMin
	newN = (n * new) / old
	return newN


def Handle_Finger(finger):
	for b in range(0,4):
		bone = finger.bone(b)
		Handle_Bone(bone, 4 - b )


def Handle_Bone(bone, width):
	base = bone.prev_joint
	tip = bone.next_joint
	xBase, yBase = Handle_Vector_FromLeap(base)
	xTip, yTip = Handle_Vector_FromLeap(tip)

	pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, width)
	#print tip, base
	#print Handle_Vector_FromLeap(tip), Handle_Vector_FromLeap(base)


def Handle_Vector_FromLeap(v):
	global xMin, xMax, yMin, yMax
	x = v[0]
	y = v[2]
	if (x < xMin):
		xMin = x
	if (x > xMax):
		xMax = x
	if (y < yMin):
		yMin = y
	if y > yMax:
		yMax = y

	x = Scale(x, xMin, xMax, 0, myConstants.pygameWindowWidth)
	y = Scale(y, xMin, xMax, 0, myConstants.pygameWindowDepth)
	#print(x,y)

	return x, y


while True:
	pygameWindow.Prepare()
	frame = controller.frame()
	if len(frame.hands) > 0:
		hand = frame.hands[0]
		Handle_Frame(frame)
		k = 0
		for finger in range(0,5):
			finger = hand.fingers[finger]
			for b in range(0,4):
				if b == 0:
                    bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
				elif b == 1:
                    bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
				elif b == 2:
                    bone = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)
				elif b == 3:
                    bone = finger.bone(Leap.Bone.TYPE_DISTAL)

				boneBase = bone.prev_joint
				boneTip = bone.next_joint

				xBase = boneBase[0]
                yBase = boneBase[1]
                zBase = boneBase[2]
                xTip  = boneTip[0]
                yTip  = boneTip[1]
                zTip  = boneTip[2]

                if ((b == 0)or(b == 3)):
                    testData[0, k] = xTip
                    testData[0, k+1] = yTip
                    testData[0, k+2] = zTip
                    k = k+3
		print(testData)
	pygameWindow.Reveal()

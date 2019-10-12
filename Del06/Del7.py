import sys
sys.path.insert(0,'../..')
from Leap import *

import numpy as np
import random
import pickle


from pygameWindow6 import PYGAME_WINDOW
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

# load in classifier
clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros((1,30),dtype='f')

k = 0


def Scale(n, oMin, oMax, newMin, newMax):
	n = n - oMin
	if(oMin == oMax):
		return n
	old = oMax - oMin
	new = newMax - newMin
	newN = (n * new) / old
	return newN


def Handle_Frame(frame):
	global x, y, xMin, xMax, yMin, yMax, k, testData
	hand = frame.hands[0]
	fingers = hand.fingers
	k = 0
	for finger in fingers:
		Handle_Finger(finger)
	#print(testData)
	#testData = CenterData(testData)
	CenterData()
	predictedClass = clf.Predict(testData)
	print(predictedClass)


def Handle_Finger(finger):
	for b in range(0,4):
		bone = finger.bone(b)
		Handle_Bone(bone, 4 - b)


def Handle_Bone(bone, width):
	global k, testData
	base = bone.prev_joint
	tip = bone.next_joint

	xBase, yBase = Handle_Vector_FromLeap(base)
	xTip, yTip = Handle_Vector_FromLeap(tip)

	pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, width)

	b = 4 - width
	if ( (b==0) or (b==3) ):
		testData[0,k] = tip[0]
		testData[0,k+1] = tip[1]
		testData[0,k+2] = tip[2]
		k = k + 3


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

def CenterData():
	global testData
	totalX = testData[0,::3]
	avgX = totalX.mean()
	testData[0,::3] = totalX - avgX

	totalY = testData[0,1::3]
	avgY = totalY.mean()
	testData[0,1::3] = totalY - avgY

	totalZ = testData[0,2::3]
	avgZ = totalZ.mean()
	testData[0,2::3] = totalZ - avgZ



while True:

	pygameWindow.Prepare()

	frame = controller.frame()
	if len(frame.hands) > 0:
		Handle_Frame(frame)
	pygameWindow.Reveal()

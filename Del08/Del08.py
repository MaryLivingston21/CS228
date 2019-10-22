import sys
sys.path.insert(0,'../..')
from Leap import *

import numpy as np
import random
import pickle
import pygame
import time


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

#load in classifier
clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros((1,30),dtype='f')
k = 0

programState = 0
xLoc = 0
yLoc = 0
numCorrect = 0
ranNumber = random.randrange(10)

# Set up Database
database = pickle.load(open('userData/database.p','rb'))
userName = raw_input('Please enter your name: ')

if userName in database:
    thing = database[userName][0]
    thing['logins'] += 1
    database[userName][0] = [thing]
    print('Welcome back ' + userName + '.')
else:
	numTimes = 1
	logins = {'logins' : 1}
	userRecord = {'digit0attempted' : 0, 'digit1attempted' : 0,
	 'digit2attempted' : 0, 'digit3attempted' : 0, 'digit4attempted' : 0,
	  'digit5attempted' : 0, 'digit6attempted' : 0, 'digit7attempted' : 0,
	   'digit8attempted' : 0, 'digit9attempted' : 0,}
	database[userName] = [logins, userRecord]
	print('Welcome ' + userName + '.')

print(database)
pickle.dump(database,open('userData/database.p','wb'))


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
	global numCorrect, ranNumber, programState
	hand = frame.hands[0]
	fingers = hand.fingers
	k = 0
	for finger in fingers:
		Handle_Finger(finger)
	#print(testData)
	#testData = CenterData(testData)
	CenterData()


def Handle_Finger(finger):
	for b in range(0,4):
		bone = finger.bone(b)
		Handle_Bone(bone, 4 - b)


def Handle_Bone(bone, width):
	global k, testData, xLoc, yLoc
	base = bone.prev_joint
	tip = bone.next_joint

	xBase, yBase = Handle_Vector_FromLeap(base)
	xTip, yTip = Handle_Vector_FromLeap(tip)

	xLoc = (myConstants.pygameWindowWidth/4 - (xBase+xTip)/2)
	yLoc = (myConstants.pygameWindowDepth/4 - (yBase+yTip)/2)

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

	x = Scale(x, xMin, xMax, 0, myConstants.pygameWindowWidth/2)
	y = Scale(y, yMin, yMax, 0, myConstants.pygameWindowDepth/2)
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

def HandOverDevice():
    # #if the list is not empty
	if(len(frame.hands) > 0):
		return True
	else:
		return False

def isCentered():
	global xLoc, yLoc
	if xLoc > myConstants.pygameWindowWidth/8:
		#print("move right")
		pygameWindow.moveRight()
	elif xLoc < -(myConstants.pygameWindowWidth/8):
		#print("move left")
		pygameWindow.moveLeft()
	elif yLoc > myConstants.pygameWindowDepth/8:
		#print("move down")
		pygameWindow.moveDown()
	elif yLoc < -(myConstants.pygameWindowDepth/30):
		#print ("move up")
		pygameWindow.moveUp()
	else:
		#pygameWindow.success()
		return True
	return False

def HandleState0():
	global programState
	pygameWindow.drawImage()
	if HandOverDevice():
		programState = 1

def HandleState1():
	global programState
	if isCentered():
		programState = 2
	else:
		programState = 1
	if HandOverDevice() == False:
		programState = 0

def HandleState2():
	global programState, testData, numCorrect, ranNumber, database, userName

	pygameWindow.numAttempt(database, userName, ranNumber)

	pygameWindow.showNum(ranNumber)
	pygameWindow.showSign(ranNumber)

	predictedClass = clf.Predict(testData)
	print(predictedClass)
	#print(numCorrect)
	if (predictedClass == ranNumber):
		numCorrect += 1
	else:
		numCorrect = 0

	if (numCorrect >= 10):
		pygameWindow.success()
		HandleAttempt()
		programState = 3
	elif isCentered():
		programState = 2
	else:
		programState = 1
	if HandOverDevice() == False:
		programState = 0

def HandleState3():
	global programState, numCorrect, ranNumber


	numCorrect = 0
	ranNumber = random.randrange(10)


	if HandOverDevice() == False:
		programState = 0
	if isCentered():
		programState = 2
	else:
		programState = 1

def HandleAttempt():
	global ranNumber, database, userName
	if (ranNumber == 0):
		userRecord = database[userName][1]
		userRecord['digit0attempted'] = userRecord['digit0attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 1:
		userRecord = database[userName][1]
		userRecord['digit1attempted'] = userRecord['digit1attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 2:
		userRecord = database[userName][1]
		userRecord['digit2attempted'] = userRecord['digit2attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 3:
		userRecord = database[userName][1]
		userRecord['digit3attempted'] = userRecord['digit3attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 4:
		userRecord = database[userName][1]
		userRecord['digit4attempted'] = userRecord['digit4attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 5:
		userRecord = database[userName][1]
		userRecord['digit5attempted'] = userRecord['digit5attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 6:
		userRecord = database[userName][1]
		userRecord['digit6attempted'] = userRecord['digit6attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 7:
		userRecord = database[userName][1]
		userRecord['digit7attempted'] = userRecord['digit7attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 8:
		userRecord = database[userName][1]
		userRecord['digit8attempted'] = userRecord['digit8attempted'] + 1
		database[userName][1] = userRecord
	elif ranNumber == 9:
		userRecord = database[userName][1]
		userRecord['digit9attempted'] = userRecord['digit9attempted'] + 1
		database[userName][1] = userRecord

	print(database)
	pickle.dump(database,open('userData/database.p','wb'))


while True:
	pygameWindow.Prepare()
	frame = controller.frame()

	if programState == 0:
		HandleState0()
	elif programState == 1:
		HandleState1()
	elif programState == 2:
		HandleState2()
	elif programState == 3:
		HandleState3()
		time.sleep(2)

	if len(frame.hands) > 0:
		Handle_Frame(frame)
	pygameWindow.Reveal()

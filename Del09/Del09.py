import sys
sys.path.insert(0,'../..')

from Leap import *

import numpy as np
import random
import pickle
import pygame
import time
import threading


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

numTry = 0 #num tries to match digit
numCorrect = 0 # num correct matches
ranNumber = 0
leastAttemptedNumber = 8

loop = 1 # num times user went through all the digits
numSec = 10.0 # how long sign should display before hiding
numTimesBeforeFailure = 50 # how long the window should try to get the # before it counts it as a fail
timer = None # the timer that triggers the hidden sign
isHidden = False # bool weather the sign should be hidden

firstTimeinState2 = True

# Set up Database
database = pickle.load(open('userData/database.p','rb'))
# get userName
userName = raw_input('Please enter your name: ')

if userName in database:
    thing = database[userName][0]
    thing['logins'] += 1
    database[userName][0] = [thing]
    print('Welcome back ' + userName + '.')
    loop = 2
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
    global programState, testData, numCorrect, ranNumber, database, userName, numTry, firstTimeinState2, numSec, isHidden, timer, numTimesBeforeFailure
    pygameWindow.numAttempt(database, userName, ranNumber)
    pygameWindow.showNum(ranNumber)

    getTime()

    #untill timer stops and sign is removed, show sign
    if (isHidden == False):
        pygameWindow.showSign(ranNumber)

    # starts timer when new digit is first shown
    if firstTimeinState2:
        pygameWindow.showSign(ranNumber)
        timer = threading.Timer(numSec,hideDig, args=())
        timer.start()
        print("Timer started")

    predictedClass = clf.Predict(testData)
    print(predictedClass)
    #print(numCorrect)
    numTry += 1

    if (predictedClass == ranNumber):
		numCorrect += 1
    else:
        numCorrect = 0

    # after 45 tries it counts as a fail and moves on
    if (numTry > numTimesBeforeFailure):
        pygameWindow.fail()
        programState = 3
        timer.cancel()
    elif (numCorrect >= 10):
        pygameWindow.success()
        HandleAttempt()
        programState = 3
        timer.cancel()
    elif isCentered():
        programState = 2
    else:
        programState = 1

    if HandOverDevice() == False:
        programState = 0

    firstTimeinState2 = False

def HandleState3():
    global programState, numCorrect, ranNumber, loop, numTry, firstTimeinState2, isHidden, leastAttemptedNumber

    firstTimeinState2 = True
    isHidden = False
    numCorrect = 0
    numTry = 0

    print("Loop")
    print(loop)
    if loop < 1:
        if ranNumber <= 8:
            ranNumber += 1
        else:
            ranNumber = 0
            loop += 1
    else:
        print("randomNum")
        n = random.randrange(3)
        if n == 1: # 1/3 of time, display leastAttemptedNumber
            getLeastAttemptedNumber()
            print ("NUMBER: ")
            print(leastAttemptedNumber)
            ranNumber = leastAttemptedNumber
        else:
            ranNumber = random.randrange(10)

        #ranNumber = random.randrange(10)


    if HandOverDevice() == False:
		programState = 0
    if isCentered():
        programState = 2
    else:
        programState = 1

def getLeastAttemptedNumber():
    global database, userName, leastAttemptedNumber
    userRecord = database[userName][1]
    string = 'digit' + str(leastAttemptedNumber) + 'attempted'
    valueOfLeastAttemptedNumber = userRecord[string]
    for digit,value in userRecord.iteritems():
        #print(digit[5],value)
        if value < valueOfLeastAttemptedNumber:
            num = digit[5] #get the digit of that value
            leastAttemptedNumber = int(num);
    print leastAttemptedNumber


def HandleAttempt():
	global ranNumber, database, userName

        userRecord = database[userName][1]
        string = 'digit' + str(ranNumber) + 'attempted'
        userRecord[string] = userRecord[string] + 1

	print(database)
	pickle.dump(database,open('userData/database.p','wb'))

def hideDig():
    global isHidden
    pygameWindow.hideDigit()
    isHidden = True

# determins how long before digit is hidden
def getTime():
    global numSec, ranNumber, database, userName, numTimesBeforeFailure
    userRecord = database[userName][1]
    string = 'digit' + str(ranNumber) + 'attempted'
    numberOfAttempts = userRecord[string]
    if numberOfAttempts < 2:
        numSec = 10.0
        numTimesBeforeFailure = 50
    elif numberOfAttempts < 3:
        numSec = 7.0
        numTimesBeforeFailure = 45
    elif numberOfAttempts < 5:
        numSec = 4.0
        numTimesBeforeFailure = 40
    elif numberOfAttempts < 7:
        numSec = 2.0
    elif numberOfAttempts < 10:
        numTimesBeforeFailure = 35
        numSec = 0.0
        numTimesBeforeFailure = 30

getLeastAttemptedNumber()

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

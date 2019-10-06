from pyGameWindow_Del03 import PYGAME_WINDOW
from constants import CONSTANTS

import numpy as np
import pickle
import os
import shutil

class RECORDER:
    def __init__(self,controller, pygameWindow, x, y, xMin, xMax, yMin, yMax):
        self.controller = controller
        self.pygameWindow = pygameWindow

        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.myConstants = CONSTANTS()
        self.prevNumberOfHands = 0
        self.currNumberOfHands = 0
        self.i = 0
        self.j = 0

        self.numberOfGestures = 1000
        self.gestureIndex = 0
        self.gestureData = np.zeros((5,4,6,self.numberOfGestures),dtype='f')


    def Handle_Directory(self):
        try:
            shutil.rmtree("userData")
        except:
            "directory does not exist"
        try:
            os.mkdir("userData")
        except:
            "directory exists"


    def Handle_Frame(self, frame):
        self.i = 0
        hand = frame.hands[0]
        self.currNumberOfHands = len(frame.hands)
        fingers = hand.fingers

        for finger in fingers:
            self.Handle_Finger(finger)
            self.i = self.i + 1

        if self.Recording_Is_Ending():
            self.Handle_Directory()
            #self.Save_Gesture()

        if self.currNumberOfHands == 2:
            print('gesture ' + str(self.gestureIndex) + ' stored.')
            self.gestureIndex = self.gestureIndex + 1
            if self.gestureIndex == self.numberOfGestures:
                self.Save_Gesture()
                exit(0)


    def Scale(self, n, oMin, oMax, newMin, newMax):
    	n = n - oMin
    	if(oMin == oMax):
    		newN = n
    		return newN
    	old = oMax - oMin
    	new = newMax - newMin
    	newN = (n * new) / old
    	return newN


    def Handle_Finger(self, finger):
        self.j = 0
        for b in range(0,4):
            bone = finger.bone(b)
            self.Handle_Bone(bone, 4 - b )
            self.j = self.j + 1


    def Handle_Bone(self, bone, width):
    	self.base = bone.prev_joint
    	self.tip = bone.next_joint
        if (self.currNumberOfHands == 1):
            self.pygameWindow.Draw_Lines(self.Handle_Vector_FromLeap(self.tip), self.Handle_Vector_FromLeap(self.base), width, (0,255,0))
        elif (self.currNumberOfHands == 2):
            self.pygameWindow.Draw_Lines(self.Handle_Vector_FromLeap(self.tip), self.Handle_Vector_FromLeap(self.base), width, (255,0,0))

            #print(self.gestureData)
        #if self.Recording_Is_Ending():
            #self.gestureData[self.i,self.j,0] = self.base[0]
            #self.gestureData[self.i,self.j,1] = self.base[1]
            #self.gestureData[self.i,self.j,2] = self.base[2]
            #self.gestureData[self.i,self.j,3] = self.tip[0]
            #self.gestureData[self.i,self.j,4] = self.tip[1]
            #self.gestureData[self.i,self.j,5] = self.tip[2]
    	#print tip, base
    	#print Handle_Vector_FromLeap(tip), Handle_Vector_FromLeap(base)

        if (self.currNumberOfHands == 2):
            self.gestureData[self.i, self.j, 0, self.gestureIndex] = self.base[0]
            self.gestureData[self.i, self.j, 1, self.gestureIndex] = self.base[1]
            self.gestureData[self.i, self.j, 2, self.gestureIndex] = self.base[2]
            self.gestureData[self.i, self.j, 3, self.gestureIndex] = self.tip[0]
            self.gestureData[self.i, self.j, 4, self.gestureIndex] = self.tip[1]
            self.gestureData[self.i, self.j, 5, self.gestureIndex] = self.tip[2]


    def Handle_Vector_FromLeap(self, v):
    	self.x = self.Scale(v[0], self.xMin, self.xMax, 0, self.myConstants.pygameWindowWidth)
    	self.y = self.Scale(v[2], self.yMin, self.yMax, 0, self.myConstants.pygameWindowDepth)
    	#print(self.x,self.y)

    	if (self.x < self.xMin):
    		self.xMin = self.x
    	if (self.x > self.xMax):
    		self.xMax = self.x
    	if (self.y < self.yMin):
    		self.yMin = self.y
    	if (self.y > self.yMax):
    		self.yMax = self.y
    	return self.x, self.y

    def Run_Once(self):
        self.pygameWindow.Prepare()
        frame = self.controller.frame()
        if len(frame.hands) != 0:
            self.Handle_Frame(frame)
        self.pygameWindow.Reveal()
        self.prevNumberOfHands = self.currNumberOfHands


    def Run_Forever(self):
        while True:
            self.Run_Once()

    def Recording_Is_Ending(self):
        if (self.currNumberOfHands == 1 and self.prevNumberOfHands == 2):
            return True
        else:
            return False

    def Save_Gesture(self):
        save_gesture = open("userData/gesture.p", "w")
        pickle.dump(self.gestureData, save_gesture)
        save_gesture.close()

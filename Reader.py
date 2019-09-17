import numpy
import pickle
import os
import time

from constants import CONSTANTS
from pygameWindow_Del03 import PYGAME_WINDOW

class READER:
    def __init__(self):
        self.myconsts = CONSTANTS()
        self.getNumData('userData')
        self.xMin = self.myconsts.pygameWindowWidth
        self.xMax = -self.myconsts.pygameWindowWidth
        self.yMin = self.myconsts.pygameWindowDepth
        self.yMax = -self.myconsts.pygameWindowDepth

        self.pygameWindow = PYGAME_WINDOW()


    def getNumData(self, fileName):
        path, dirs, files = next(os.walk(fileName))
        self.numGestures = len(files)
        #print(self.numGestures)
        #for gesture in range(self.numGestures):


    # def Print_Gestures(self):
    #     for gesture in range(self.numGestures):
    #         hi = 'userData/gesture' + str(gesture) + '.p'
    #         thing = open(hi,'rb')
    #         obj = pickle.load(thing)
    #         print obj
    #         thing.close()

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()


    def Draw_Each_Gesture_Once(self):
        for gesture in range(self.numGestures):
            #print(gesture)
            self.Draw_Gesture(gesture)


    def Draw_Gesture(self, n):
        self.pygameWindow.Prepare()

        file_in = open("userData/gesture" + str(n)+ ".p", "rb")
        gestureData = pickle.load(file_in)
        file_in.close()
        for numFing in range(5):
            for numBone in range(4):
                currentBone = gestureData[numFing,numBone,:]
                xBaseNotScaled = currentBone[0]
                yBaseNotScaled = currentBone[2] # why z?
                xTipNotScaled = currentBone[3]
                yTipNotScaled = currentBone[5] #why z?


                self.pygameWindow.Draw_Line(self.Scale(currentBone[0:3],0,self.myconsts.pygameWindowWidth),self.Scale(currentBone[3:6],0,self.myconsts.pygameWindowDepth),4,(0,0,255))
        self.pygameWindow.Reveal()
        time.sleep(0.3)

    def Scale(self, (x,y,z), newMin, newMax):
        if(self.xMin == newMax):
            return x, y, z
        x = x - self.xMin
        y = y - self.yMin
        z = z - self.yMin
        old = self.xMax - self.xMin
        new = newMax - newMin
        newX = (x * new) / old
        newY = (y * new) / old
        newZ = (z * new) / old
        return newX, newY, newZ

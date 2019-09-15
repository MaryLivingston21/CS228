from pygameWindow import PYGAME_WINDOW
from constants import CONSTANTS

class DELIVERABLE:
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
        #self.numberOfHands = 0


    def Handle_Frame(self, frame):
    	hand = frame.hands[0]
    	fingers = hand.fingers

    	for finger in fingers:
    		self.Handle_Finger(finger)


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
    	for b in range(0,4):
    		bone = finger.bone(b)
    		self.Handle_Bone(bone, 4 - b )


    def Handle_Bone(self, bone, width):
    	base = bone.prev_joint
    	tip = bone.next_joint

    	self.pygameWindow.Draw_Black_Line(self.Handle_Vector_FromLeap(tip), self.Handle_Vector_FromLeap(base), width)
    	#print tip, base
    	#print Handle_Vector_FromLeap(tip), Handle_Vector_FromLeap(base)


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


    def Run_Forever(self):
        while True:
            self.Run_Once()

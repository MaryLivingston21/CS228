import sys
sys.path.insert(0,'..')
from Leap import *


from  pyGameWindow_Del03 import PYGAME_WINDOW
from constants import CONSTANTS
from Recorder import RECORDER

myConstants = CONSTANTS()

recorder = RECORDER(Controller(), PYGAME_WINDOW(), int(myConstants.pygameWindowWidth / 2), int(myConstants.pygameWindowDepth / 2), 1000, -1000, 1000, -1000)
recorder.Run_Forever();

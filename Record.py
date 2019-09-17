import sys
sys.path.insert(0,'..')
from Leap import *


from pygameWindow_Del03 import PYGAME_WINDOW
from constants import CONSTANTS
from Deliverable import DELIVERABLE

myConstants = CONSTANTS()


deliverable = DELIVERABLE(Controller(), PYGAME_WINDOW(), int(myConstants.pygameWindowWidth / 2), int(myConstants.pygameWindowDepth / 2), 1000, -1000, 1000, -1000)
deliverable.Run_Forever();

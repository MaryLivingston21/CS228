import numpy
import pickle

class READER:
    def __init__(self):
        file_in = open("userData/gesture.p","rb")
        gestureData = pickle.load(file_in)
        print gestureData

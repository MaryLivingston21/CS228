import numpy as np
import pickle

pickle_in = open("userData/gesture.p", "rb")
gestureData = pickle.load(pickle_in)
print(gestureData.shape)

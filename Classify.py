import numpy as np
import pickle

pickle_in = open("userData/train4.p", "rb")
train4 = pickle.load(pickle_in)

pickle_in = open("userData/train5.p", "rb")
train5 = pickle.load(pickle_in)

pickle_in = open("userData/test4.p", "rb")
test4 = pickle.load(pickle_in)

pickle_in = open("userData/test5.p", "rb")
test5 = pickle.load(pickle_in)

def ReshapeData(set1, set2):
    X = np.zeros((2000,5*4*6),dtype='f')
    Y = np.zeros(2000)
    for row in range(0,1000):
        Y[row] = 1
        Y[row+1000] = 2
        col = 0
        for finger in range(0,5):
            for bone in range(0,4):
                for cord in range(0,6):
                    X[row,col] = set1[finger,bone,cord,row]
                    X[row+1000,col] = set2[finger,bone,cord,row]
                    col = col + 1
    return X, Y

trainX, trainY = ReshapeData(train4,train5)
testX, testY = ReshapeData(test4, test5)

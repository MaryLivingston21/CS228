import numpy as np
import pickle
from knn import KNN

knn = KNN()


def ReshapeData(set1, set2, set3):
    X = np.zeros((3000,5*2*3),dtype='f')
    Y = np.zeros(3000, dtype='f')
    for row in range(0,1000):
        Y[row] = 4
        Y[row+1000] = 5
        Y[row+2000] = 0
        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for cord in range(0,3):
                    X[row,col] = set1[finger,bone,cord,row]
                    X[row+1000,col] = set2[finger,bone,cord,row]
                    X[row+2000,col] = set3[finger,bone,cord,row]
                    col = col + 1
    return X, Y


def ReduceData(X):
    X = np.delete(X,1,1)
    X = np.delete(X,1,1)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    X = np.delete(X,0,2)
    return X


def CenterData(X):
    allXCoordinates = X[:,:,0,:]
    meanValueX = allXCoordinates.mean()
    X[:,:,0,:] = allXCoordinates - meanValueX
    allYCoordinates = X[:,:,1,:]
    meanValueY = allYCoordinates.mean()
    X[:,:,1,:] = allYCoordinates - meanValueY
    allZCoordinates = X[:,:,2,:]
    meanValueZ = allZCoordinates.mean()
    X[:,:,2,:] = allZCoordinates - meanValueZ
    return X


pickle_in = open("userData/Livingston_train4.p", "rb")
train4 = pickle.load(pickle_in)
pickle_in = open("userData/Livingston_test4.p", "rb")
test4 = pickle.load(pickle_in)

pickle_in = open("userData/Livingston_train5.p", "rb")
train5 = pickle.load(pickle_in)
pickle_in = open("userData/Livingston_test5.p", "rb")
test5 = pickle.load(pickle_in)

pickle_in = open("userData/Childs_train0.p", "rb")
train0 = pickle.load(pickle_in)
pickle_in = open("userData/Childs_test0.p","rb")
test0 = pickle.load(pickle_in)

train4 = ReduceData(train4)
test4 = ReduceData(test4)
train5 = ReduceData(train5)
test5 = ReduceData(test5)
train0 = ReduceData(train0)
test0 = ReduceData(test0)

train4 = CenterData(train4)
test4 = CenterData(test4)
train5 = CenterData(train5)
test5 = CenterData(test5)
test0 = CenterData(test0)
test0 = CenterData(test0)

trainX, trainY = ReshapeData(train4, train5, train0)
testX, testY = ReshapeData(test4, test5, test0)

knn.Use_K_Of(15)
knn.Fit(trainX,trainY)

numCorrect = 0
for row in range(0,2000):
    prediction = int(knn.Predict(testX[row]))
    if (prediction==int(testY[row])):
        numCorrect += 1

percCorrect = (float(numCorrect)/2000.0)*100.0
print percCorrect

pickle.dump(knn, open('userData/classifier.p','wb'))

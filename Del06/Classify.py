import numpy as np
import pickle
from knn import KNN

knn = KNN()


def ReshapeData(set0,set1,set2,set3,set4,set5,set6,set7,set8,set9,set42,set72,set82,set22):
    X = np.zeros((14000,5*2*3),dtype='f')
    Y = np.zeros(14000, dtype='f')
    for row in range(0,1000):
        Y[row] = 0
        Y[row+1000] = 1
        Y[row+2000] = 2
        Y[row+3000] = 3
        Y[row+4000] = 4
        Y[row+5000] = 5
        Y[row+6000] = 6
        Y[row+7000] = 7
        Y[row+8000] = 8
        Y[row+9000] = 9
        Y[row+10000] = 4
        Y[row+11000] = 7
        Y[row+12000] = 8
        Y[row+13000] = 2

        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for cord in range(0,3):
                    X[row,col] = set0[finger,bone,cord,row]
                    X[row+1000,col] = set1[finger,bone,cord,row]
                    X[row+2000,col] = set2[finger,bone,cord,row]
                    X[row+3000,col] = set3[finger,bone,cord,row]
                    X[row+4000,col] = set4[finger,bone,cord,row]
                    X[row+5000,col] = set5[finger,bone,cord,row]
                    X[row+6000,col] = set6[finger,bone,cord,row]
                    X[row+7000,col] = set7[finger,bone,cord,row]
                    X[row+8000,col] = set8[finger,bone,cord,row]
                    X[row+9000,col] = set9[finger,bone,cord,row]
                    X[row+10000,col] = set42[finger,bone,cord,row]
                    X[row+11000,col] = set72[finger,bone,cord,row]
                    X[row+12000,col] = set82[finger,bone,cord,row]
                    X[row+13000,col] = set22[finger,bone,cord,row]
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

pickle_in = open("userData/Childs_train0.p", "rb")
train0 = pickle.load(pickle_in)
pickle_in = open("userData/Childs_test0.p","rb")
test0 = pickle.load(pickle_in)

pickle_in = open("userData/Newton_train1.p", "rb")
train1 = pickle.load(pickle_in)
pickle_in = open("userData/Newton_test1.p","rb")
test1 = pickle.load(pickle_in)

pickle_in = open("userData/Gordon_train2.p", "rb")
train2 = pickle.load(pickle_in)
pickle_in = open("userData/Gordon_test2.p","rb")
test2 = pickle.load(pickle_in)

pickle_in = open("userData/Trinity_train2.p", "rb")
train2_2 = pickle.load(pickle_in)
pickle_in = open("userData/Trinity_test2.p","rb")
test2_2 = pickle.load(pickle_in)

pickle_in = open("userData/Beatty_train3.p", "rb")
train3 = pickle.load(pickle_in)
pickle_in = open("userData/Beatty_test3.p","rb")
test3 = pickle.load(pickle_in)

pickle_in = open("userData/Livingston_train4.p", "rb")
train4 = pickle.load(pickle_in)
pickle_in = open("userData/Livingston_test4.p", "rb")
test4 = pickle.load(pickle_in)

pickle_in = open("userData/Ogilvie_train4.p", "rb")
train4_2 = pickle.load(pickle_in)
pickle_in = open("userData/Ogilvie_test4.p", "rb")
test4_2 = pickle.load(pickle_in)

pickle_in = open("userData/Livingston_train5.p", "rb")
train5 = pickle.load(pickle_in)
pickle_in = open("userData/Livingston_test5.p", "rb")
test5 = pickle.load(pickle_in)

pickle_in = open("userData/Peck_train6.p", "rb")
train6 = pickle.load(pickle_in)
pickle_in = open("userData/Peck_test6.p", "rb")
test6 = pickle.load(pickle_in)

pickle_in = open("userData/Picard_train7.p", "rb")
train7 = pickle.load(pickle_in)
pickle_in = open("userData/Picard_test7.p", "rb")
test7 = pickle.load(pickle_in)

pickle_in = open("userData/Rubin_train7.p", "rb")
train7_2 = pickle.load(pickle_in)
pickle_in = open("userData/Rubin_test7.p", "rb")
test7_2 = pickle.load(pickle_in)

pickle_in = open("userData/Burleson_train8.p", "rb")
train8 = pickle.load(pickle_in)
pickle_in = open("userData/Burleson_test8.p", "rb")
test8 = pickle.load(pickle_in)

pickle_in = open("userData/Mardis_train8.p", "rb")
train8_2 = pickle.load(pickle_in)
pickle_in = open("userData/Mardis_test8.p", "rb")
test8_2 = pickle.load(pickle_in)

pickle_in = open("userData/Saulean_train9.p", "rb")
train9 = pickle.load(pickle_in)
pickle_in = open("userData/Saulean_test9.p", "rb")
test9 = pickle.load(pickle_in)


train0 = ReduceData(train0)
test0 = ReduceData(test0)
train1 = ReduceData(train1)
test1 = ReduceData(test1)
train2 = ReduceData(train2)
test2 = ReduceData(test2)
train3 = ReduceData(train3)
test3 = ReduceData(test3)
train4 = ReduceData(train4)
test4 = ReduceData(test4)
train5 = ReduceData(train5)
test5 = ReduceData(test5)
train6 = ReduceData(train6)
test6 = ReduceData(test6)
train7 = ReduceData(train7)
test7 = ReduceData(test7)
train8 = ReduceData(train8)
test8 = ReduceData(test8)
train9 = ReduceData(train9)
test9 = ReduceData(test9)
train2_2 = ReduceData(train2_2)
test2_2 = ReduceData(test2_2)
train4_2 = ReduceData(train4_2)
test4_2 = ReduceData(test4_2)
train7_2 = ReduceData(train7_2)
test7_2 = ReduceData(test7_2)
train8_2 = ReduceData(train8_2)
test8_2 = ReduceData(test8_2)

train0 = CenterData(train0)
test0 = CenterData(test0)
train1 = CenterData(train1)
test1 = CenterData(test1)
train2 = CenterData(train2)
test2 = CenterData(test2)
train3 = CenterData(train3)
test3 = CenterData(test3)
train4 = CenterData(train4)
test4 = CenterData(test4)
train5 = CenterData(train5)
test5 = CenterData(test5)
train6 = CenterData(train6)
test6 = CenterData(test6)
train7 = CenterData(train7)
test7 = CenterData(test7)
train8 = CenterData(train8)
test8 = CenterData(test8)
train9 = CenterData(train9)
test9 = CenterData(test9)
train2_2 = CenterData(train2_2)
test2_2 = CenterData(test2_2)
train4_2 = CenterData(train4_2)
test4_2 = CenterData(test4_2)
train7_2 = CenterData(train7_2)
test7_2 = CenterData(test7_2)
train8_2 = CenterData(train8_2)
test8_2 = CenterData(test8_2)



trainX, trainY = ReshapeData(train0,train1,train2,train3,train4,train5,train6,train7,train8,train9,train4_2,train7_2,train8_2,train2_2)
testX, testY = ReshapeData(test0,test1,test2,test3,test4,test5,test6,test7,test8,test9,test4_2,test7_2,test8_2,test2_2)

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

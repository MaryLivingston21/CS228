import matplotlib.pyplot as plt
import numpy as np

from knn import KNN


knn = KNN()
knn.Load_Dataset('iris.csv')

x = knn.data[:,0]
y = knn.data[:,1]

trainX = knn.data[::2,1:3]
trainy = knn.target[::2]
testX = knn.data[1::2,1:3]
testy = knn.target[1::2]


knn.Use_K_Of(15)
knn.Fit(trainX,trainy)

for i in range(0, len(testy)):
    actualClass = testy[i]
    prediction = knn.Predict(testX[i,1:3])

colors = np.zeros((3,3), dtype='f')
colors[0,:] = [1,0.5,0.5] #red
colors[1,:] = [0.5,1,0.5] #light green
colors[2,:] = [0.5,0.5,1] #light blue

plt.figure()
#plt.scatter(testX[:,0], testX[:,1], c=testy)
#plt.scatter(trainX[:,0], trainX[:,1], c=trainy)
[numItems,numFeatures] = knn.data.shape
for i in range(0,numItems/2):
    itemClass = int(trainy[i]) #extracts ith item
    currColor = colors[itemClass,:] #creates red green blue vector
    plt.scatter(trainX[i,0],trainX[i,1],facecolor=currColor, s=50, lw=2)

numCorrect = 0
for i in range (0,numItems/2):
    itemClass = int(testy[i])
    prediction = int(knn.Predict(testX[i,:]))
    if (prediction == itemClass):
        numCorrect += 1
    edgeColor = colors[prediction,:]
    currColor = colors[itemClass,:]
    plt.scatter(testX[i,0], testX[i,1], facecolor=currColor, s=50, lw=2, edgecolor=edgeColor)

print(float(numCorrect)/(numItems/2) * 100.0,'%')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

from knn import KNN


knn = KNN()
knn.Load_Dataset('iris.csv')

x = knn.data[:,0]
y = knn.data[:,1]

trainX = knn.data[::2,0:2]
trainy = knn.target[::2]

testX = knn.data[1::2,1:3]
testy = knn.target[1::2]

colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1,0.5,0.5] #red
colors[1,:] = [0.5,1,0.5] #light green
colors[2,:] = [0.5,0.5,1] #light blue

plt.figure()
plt.scatter(trainX[:,0], trainX[:,1], c=trainy)
plt.scatter(testX[:,0], testX[:,1], c=testy)
plt.show()

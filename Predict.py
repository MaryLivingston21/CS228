import matplotlib.pyplot as plt

from knn import KNN


knn = KNN()
knn.Load_Dataset('iris.csv')
print(knn.target)

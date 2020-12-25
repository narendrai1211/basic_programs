from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier  # Import KNN (K - nearest neighbour)

dataset_iris = load_iris()
# print(dataset_iris)
# print(dataset_iris.target)
# print(dataset_iris.target_names)
# All are numpy arrays and faster that regular lists
# print(type(dataset_iris.target))
d = dataset_iris.data.shape
# print(d)
# print(type(d))  # neighbours
knn = KNeighborsClassifier(3)
X = dataset_iris.data
Y = dataset_iris.target
knn.fit(X, Y)
print(knn.predict([[1, 3, 6, 4.8]]))

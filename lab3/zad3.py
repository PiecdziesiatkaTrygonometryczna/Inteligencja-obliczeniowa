import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("iris.csv")
#  a


train_set, test_set = train_test_split(df, train_size=0.7, random_state=483483)

train_inputs = train_set.drop('species', axis=1)
train_classes = train_set['species']
test_inputs = test_set.drop('species', axis=1)
test_classes = test_set['species']


arr = [3,5,11]

#  b


for i in arr:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_inputs, train_classes)
    knn_predictions = knn.predict(test_inputs)
    knn_accuracy = accuracy_score(test_classes, knn_predictions)
    knn_conf_matrix = confusion_matrix(test_classes, knn_predictions)
    print(f"Dokładność klasyfikatora {i}-NN:", knn_accuracy)
    print(f"Macierz błędów klasyfikatora {i}-NN:")
    print(knn_conf_matrix)


naive_bayes = GaussianNB()
naive_bayes.fit(train_inputs, train_classes)
naive_bayes_predictions = naive_bayes.predict(test_inputs)
naive_bayes_accuracy = accuracy_score(test_classes, naive_bayes_predictions)
naive_bayes_conf_matrix = confusion_matrix(test_classes, naive_bayes_predictions)


print("Dokładność klasyfikatora Naive Bayes:", naive_bayes_accuracy)
print("Macierz błędów klasyfikatora Naive Bayes:")
print(naive_bayes_conf_matrix)


# Dokładność klasyfikatora 3-NN: 0.9555555555555556
# Macierz błędów klasyfikatora 3-NN:
# [[14  0  0]
#  [ 0 12  0]
#  [ 0  2 17]]
# Dokładność klasyfikatora 5-NN: 0.9111111111111111
# Macierz błędów klasyfikatora 5-NN:
# [[14  0  0]
#  [ 0 12  0]
#  [ 0  4 15]]
# Dokładność klasyfikatora 11-NN: 0.9333333333333333
# Macierz błędów klasyfikatora 11-NN:
# [[14  0  0]
#  [ 0 12  0]
#  [ 0  3 16]]
# Dokładność klasyfikatora Naive Bayes: 0.9555555555555556
# Macierz błędów klasyfikatora Naive Bayes:
# [[14  0  0]
#  [ 0 12  0]
#  [ 0  2 17]]

# c

# największą dokładność miał klasyfikator drzewa decyzyjnego z zadania 2
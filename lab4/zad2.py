import pandas as pd
df = pd.read_csv("iris.csv")
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

#A


(train_set, test_set) = train_test_split(df.values, train_size=0.7, 
random_state=13)

#B


train_labels = train_set[:, -1]
test_labels = test_set[:, -1]

print(test_labels)

label_encoder = LabelEncoder()
train_labels_encoded = label_encoder.fit_transform(train_labels)
test_labels_encoded = label_encoder.transform(test_labels)

# print(train_labels_encoded)
#  [1 1 1 1 1 1 2 1 1 1 0 0 0 2 0 2 2 2 0 1 1 2 0 0 2 0 0 1 1 1 0 0 2 0 1 2 1
#  1 2 2 0 1 2 0 1 0 1 2 0 1 1 2 1 1 0 1 2 0 1 2 2 0 0 0 0 0 1 0 2 0 0 1 0 2
#  2 0 2 2 1 0 0 1 1 2 2 0 0 0 0 0 1 1 2 1 2 2 0 1 1 1 2 0 2 0 1]


# print(test_labels_encoded)
# [2 0 2 1 2 0 2 2 0 2 0 0 2 0 2 1 1 2 2 1 2 0 1 2 1 0 1 2 0 2 2 2 1 2 1 0 1
#  2 1 0 2 2 0 2 1]


# print(label_encoder.classes_)
# ['setosa' 'versicolor' 'virginica']



#D 


# model = MLPClassifier(hidden_layer_sizes=(2,), activation='relu', solver='adam', max_iter=5000)
# model.fit(train_set[:, :-1], train_labels_encoded)


# #E


# train_accuracy = model.score(train_set[:, :-1], train_labels_encoded)
# test_accuracy = model.score(test_set[:, :-1], test_labels_encoded)

# print("score on train data:", train_accuracy)
# print("score on test data:", test_accuracy)

# score on train data: 0.9619047619047619
# score on test data: 0.9333333333333333


#F

# model_3_neurons = MLPClassifier(hidden_layer_sizes=(3,), activation='relu', solver='adam', max_iter=5000)
# model_3_neurons.fit(train_set[:, :-1], train_labels_encoded)

# train_accuracy_3_neurons = model_3_neurons.score(train_set[:, :-1], train_labels_encoded)
# test_accuracy_3_neurons = model_3_neurons.score(test_set[:, :-1], test_labels_encoded)

# print("score on train data with 3 neurons:", train_accuracy_3_neurons)
# print("score on test data with 3 neurons:", test_accuracy_3_neurons)

# score on train data with 3 neurons: 0.9714285714285714
# score on test data with 3 neurons: 0.9555555555555556


#G

# model_2_layers = MLPClassifier(hidden_layer_sizes=(3, 3), activation='relu', solver='adam', max_iter=5000)
# model_2_layers.fit(train_set[:, :-1], train_labels_encoded)

# train_accuracy_2_layers = model_2_layers.score(train_set[:, :-1], train_labels_encoded)
# test_accuracy_2_layers = model_2_layers.score(test_set[:, :-1], test_labels_encoded)


# print("score on train data with 2 layers:", train_accuracy_2_layers)
# print("score on test data with 2 layers:", test_accuracy_2_layers)

# score on train data with 2 layers: 0.9714285714285714
# score on test data with 2 layers: 0.9777777777777777
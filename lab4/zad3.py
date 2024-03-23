import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# A
df = pd.read_csv("diabetes 1.csv")

train_set, test_set = train_test_split(df, test_size=0.3, random_state=13)

# B

# model = MLPClassifier(hidden_layer_sizes=(6, 3), activation='relu', max_iter=500, random_state=13)

# # C

# model.fit(train_set.drop(columns=['class']), train_set['class'])

# # D

# predictions = model.predict(test_set.drop(columns=['class']))

# accuracy = accuracy_score(test_set['class'], predictions)
# print("accuracy:", accuracy)

# conf_matrix = confusion_matrix(test_set['class'], predictions)
# print("confusion matrix:")
# print(conf_matrix)

# accuracy: 0.70995670995671
# confusion matrix:
# [[123  26]
#  [ 41  41]]

# E

model = MLPClassifier(hidden_layer_sizes=(10, 5), activation='tanh', max_iter=5000, random_state=13)
model.fit(train_set.drop(columns=['class']), train_set['class'])
predictions = model.predict(test_set.drop(columns=['class']))

accuracy = accuracy_score(test_set['class'], predictions)
print("accuracy:", accuracy)

conf_matrix = confusion_matrix(test_set['class'], predictions)
print("confusion matrix:")
print(conf_matrix)

# accuracy: 0.7445887445887446
# confusion matrix: 
# [[135  14]
#  [ 45  37]]

# poradziła sobie gorzej, w poprzednich laboratoriach w działaniach na zbiorach z  irysami
# sieci osiągały dokładność powyżej 90%, w jednym przypadku nawet 97%.


# F 

# Gorsze błędy w przypadku diagnozowania chorób to oczywiście FN (Fałszywie negatywne)
# z racji na to, że lepiej jest zostać zdiagnozowanym jako chorym, przejść inne badania, i potem jednak okazać się
# zdrowym, niż zostać zdiagnozowanym jako zdrowy, w rzeczywistości będąc chorym i dać chorobie postępować,
# nie wiedząć o niej

# w tym przypadku więcej jest błędów fałszywie negatywnych (45) w stosunku do fałszywie pozytywnych (14)